# Mixture of Experts (MoE) Provider

The MoE provider creates a "Frankenstein" API-based ensemble that combines Anthropic Claude, DeepSeek, and Mistral AI to leverage the strengths of each model.

## Overview

Instead of using a single LLM provider, the MoE provider intelligently routes requests, aggregates responses, and combines the expertise of multiple models. Think of it as having a team of AI specialists working together.

## Strategies

### 1. **Task-Based Routing** (Default)

Routes requests to the best provider based on task characteristics.

**When to use:** General-purpose usage where different tasks benefit from different models

**How it works:**
- Analyzes task content for keywords
- Routes code tasks → DeepSeek
- Routes creative tasks → Mistral
- Routes analytical tasks → Claude
- Falls back to cascade if provider fails

**Configuration:**
```yaml
llm_provider:
  provider: moe
  moe:
    moe_strategy: task_based
    specialist_map:
      code: deepseek
      creative: mistral
      analysis: anthropic
```

**Example:**
```python
# "Write a Python function to parse JSON" → Routes to DeepSeek
# "Write a creative story about AI" → Routes to Mistral
# "Analyze this security vulnerability" → Routes to Claude
```

### 2. **Voting/Ensemble**

Sends request to ALL providers and uses consensus/majority voting.

**When to use:**
- Critical decisions requiring high confidence
- When accuracy is more important than speed
- Quality assurance for important outputs

**How it works:**
- Queries all 3 providers in parallel
- For short responses: uses majority vote
- For long responses: picks most detailed/complete
- Returns the "winning" response with annotation

**Configuration:**
```yaml
llm_provider:
  provider: moe
  moe:
    moe_strategy: voting
    voting_threshold: 0.5
```

**Pros:** Highest quality, catches errors, diverse perspectives
**Cons:** 3x cost, slower, requires all API keys

### 3. **Cascade/Fallback**

Tries providers in order until one succeeds.

**When to use:**
- High reliability requirements
- API outages or rate limiting
- Cost optimization (cheaper models first)

**How it works:**
- Tries first provider in fallback_order
- If it fails, tries next provider
- Continues until success or all fail
- Returns first successful response

**Configuration:**
```yaml
llm_provider:
  provider: moe
  moe:
    moe_strategy: cascade
    fallback_order:
      - deepseek  # Try cheapest first
      - mistral
      - anthropic  # Most reliable last
```

**Pros:** Maximum reliability, cost-effective
**Cons:** Slower on failures, no quality comparison

### 4. **Best-of-N**

Queries multiple providers in parallel and picks the best response.

**When to use:**
- When you need the single best answer
- Quality over consensus
- Complex reasoning tasks

**How it works:**
- Queries all available providers in parallel
- Scores each response based on:
  - Completeness (stop_reason == "end_turn")
  - Length/detail
  - Tool usage (if applicable)
- Returns highest-scoring response

**Configuration:**
```yaml
llm_provider:
  provider: moe
  moe:
    moe_strategy: best_of_n
```

**Pros:** Best individual response, parallel execution
**Cons:** Higher cost, requires judgment criteria

### 5. **Specialist**

Routes different operations to specialized providers.

**When to use:**
- Complex multi-step workflows
- Mixed workloads (code + docs + analysis)
- Advanced orchestration

**How it works:**
- Currently uses task-based routing as foundation
- Future: Split operations across providers
- Future: Parallel tool execution across providers

**Configuration:**
```yaml
llm_provider:
  provider: moe
  moe:
    moe_strategy: specialist
    specialist_map:
      # Custom mappings
```

**Status:** Foundation implemented, advanced features planned

## Configuration Reference

### Full Configuration Example

```yaml
llm_provider:
  provider: moe  # Enable MoE

  moe:
    # Strategy selection
    moe_strategy: task_based  # or: voting, cascade, best_of_n, specialist

    # Which providers to include
    moe_providers:
      - anthropic
      - deepseek
      - mistral

    # Fallback order (for cascade)
    fallback_order:
      - anthropic
      - deepseek
      - mistral

    # Task routing (for task_based/specialist)
    specialist_map:
      # Code-related keywords
      code: deepseek
      python: deepseek
      javascript: deepseek
      programming: deepseek
      function: deepseek
      debug: deepseek

      # Creative keywords
      creative: mistral
      story: mistral
      write: mistral
      compose: mistral
      narrative: mistral

      # Analytical keywords
      analysis: anthropic
      analyze: anthropic
      explain: anthropic
      research: anthropic
      security: anthropic
      vulnerability: anthropic

    # Voting parameters
    voting_threshold: 0.5  # Confidence threshold (0.0-1.0)
```

### Per-Agent MoE Override

```yaml
agents:
  # Use MoE for this specific agent
  unicode_archaeologist:
    enabled: true
    llm_provider: moe
    moe_strategy: voting  # Use voting for critical security research
    moe_providers:
      - anthropic
      - deepseek

  # Regular single-provider agent
  payload_artisan:
    enabled: true
    llm_provider: deepseek
```

## Usage Examples

### Basic Usage

```python
from agents.llm_providers import LLMProviderFactory

# Create MoE provider
provider = LLMProviderFactory.create_provider(
    "moe",
    moe_strategy="task_based",
    moe_providers=["anthropic", "deepseek", "mistral"]
)

# Make request
messages = [{"role": "user", "content": "Write a Python sorting function"}]
response = provider.create_completion(messages)

# Check which provider was used
print(response.model)  # e.g., "deepseek-chat (moe: moe-taskbased-deepseek)"
```

### Strategy Comparison

```python
from agents.llm_providers import MixtureOfExpertsProvider

strategies = ["task_based", "voting", "cascade", "best_of_n"]
messages = [{"role": "user", "content": "Explain quantum computing"}]

for strategy in strategies:
    provider = MixtureOfExpertsProvider(
        providers=["anthropic", "deepseek", "mistral"],
        strategy=strategy
    )

    response = provider.create_completion(messages)
    print(f"\n{strategy}: {response.model}")
    print(f"Tokens: {response.usage['total_tokens']}")
    print(f"Response: {response.content[0]['text'][:100]}...")
```

### Dynamic Strategy Selection

```python
def select_moe_strategy(task: str, importance: str) -> str:
    """Select MoE strategy based on task characteristics."""

    if importance == "critical":
        return "voting"  # Highest quality

    if "code" in task.lower():
        return "task_based"  # Route to best provider

    if importance == "high":
        return "best_of_n"  # Quality over speed

    return "cascade"  # Reliability + cost

# Use selected strategy
task = "Write a security audit script"
strategy = select_moe_strategy(task, importance="high")

provider = LLMProviderFactory.create_provider(
    "moe",
    moe_strategy=strategy
)
```

### Agent with MoE

```python
from agents.base.agent import BaseAgent, AgentCapability

class SecurityAnalyst(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="security_analyst",
            name="Security Analyst",
            description="Multi-provider security analysis",
            capabilities=[AgentCapability.ANALYSIS],
            config={
                'llm_provider': 'moe',
                'moe_strategy': 'voting',  # Use voting for security
                'moe_providers': ['anthropic', 'deepseek', 'mistral']
            }
        )

    def run(self, task, context=None):
        self.start()

        messages = [{"role": "user", "content": task}]
        response = self.call_llm(messages, tools=self.get_tools())

        # Response comes from MoE voting ensemble
        result = self._process_response(response)

        self.complete(result)
        return result

    def get_tools(self):
        return self.toolkit.get_noseeum_tools()
```

## Performance Characteristics

| Strategy | Speed | Cost | Quality | Reliability |
|----------|-------|------|---------|-------------|
| **task_based** | ⚡⚡⚡ Fast | 💰 1x | ⭐⭐⭐ Good | 🛡️🛡️ Medium |
| **voting** | ⚡ Slow | 💰💰💰 3x | ⭐⭐⭐⭐⭐ Excellent | 🛡️🛡️🛡️ High |
| **cascade** | ⚡⚡ Medium | 💰 1x-3x | ⭐⭐ Fair | 🛡️🛡️🛡️🛡️ Excellent |
| **best_of_n** | ⚡ Slow | 💰💰💰 3x | ⭐⭐⭐⭐ Very Good | 🛡️🛡️🛡️ High |
| **specialist** | ⚡⚡⚡ Fast | 💰 1x | ⭐⭐⭐ Good | 🛡️🛡️ Medium |

## Cost Optimization

### Cost-Effective Strategies

1. **task_based (Default)** - Only queries 1 provider per request
2. **cascade** - Only pays for successful provider (+ failed attempts)

### Higher-Cost Strategies

1. **voting** - Always queries all 3 providers (3x cost)
2. **best_of_n** - Always queries all 3 providers (3x cost)

### Hybrid Approach

```yaml
# Use cheap providers for most tasks, expensive for critical
agents:
  routine_agent:
    llm_provider: moe
    moe_strategy: task_based  # 1x cost

  critical_agent:
    llm_provider: moe
    moe_strategy: voting  # 3x cost but highest quality
```

## Monitoring & Debugging

### Check MoE Configuration

```python
from agents.llm_providers import MixtureOfExpertsProvider

provider = MixtureOfExpertsProvider()

info = provider.get_strategy_info()
print(info)
# {
#     "provider": "moe",
#     "strategy": "task_based",
#     "available_providers": ["anthropic", "deepseek", "mistral"],
#     "total_providers": 3,
#     ...
# }
```

### Response Metadata

MoE responses include strategy information in the model field:

```python
response = provider.create_completion(messages)
print(response.model)
# Examples:
# "deepseek-chat (moe: moe-taskbased-deepseek)"
# "claude-sonnet-4-5-20250929 (moe: moe-voting-anthropic)"
# "mistral-large-latest (moe: moe-bestof-mistral)"
```

### Logging

MoE provider logs all routing decisions:

```
[MoE] Using TASK_BASED strategy
[MoE] Task routed to deepseek (scores: {'deepseek': 3, 'anthropic': 0, 'mistral': 0})
[MoE] Got response from deepseek
```

## Troubleshooting

### No Providers Available

**Problem:** `MoE: No providers available`

**Solutions:**
1. Set API keys: `export ANTHROPIC_API_KEY=...`
2. Check at least one provider has valid API key
3. Verify providers list in config

### All Providers Failed

**Problem:** All providers return errors in voting/best_of_n

**Solutions:**
1. Check API keys are valid
2. Verify network connectivity
3. Check rate limits on APIs
4. Review error logs for specific failures

### Unexpected Provider Selection

**Problem:** Task routed to wrong provider

**Solution:** Update specialist_map in config:

```yaml
specialist_map:
  # Add your custom keywords
  myframework: deepseek
  mylanguage: mistral
```

### High Costs

**Problem:** MoE is expensive

**Solutions:**
1. Use task_based strategy (1x cost) instead of voting/best_of_n (3x)
2. Limit moe_providers to 2 providers instead of 3
3. Use cascade with cheaper providers first
4. Reserve MoE for critical agents only

## Best Practices

### 1. Start with task_based

```yaml
moe_strategy: task_based  # Good default
```

### 2. Use voting for critical decisions

```yaml
# Security audit agent
moe_strategy: voting
moe_providers:
  - anthropic  # Known for safety
  - deepseek
```

### 3. Optimize specialist_map for your domain

```yaml
specialist_map:
  # Your specific domain keywords
  blockchain: deepseek
  regulation: anthropic
  marketing: mistral
```

### 4. Cascade for reliability on a budget

```yaml
moe_strategy: cascade
fallback_order:
  - deepseek  # Cheapest first
  - mistral
  - anthropic  # Most reliable last
```

### 5. Monitor and iterate

```python
# Log which providers are used
response = provider.create_completion(messages)
logger.info(f"MoE used: {response.model}")

# Adjust specialist_map based on results
```

## Future Enhancements

- **Parallel tool execution:** Different tools to different providers
- **Confidence scoring:** Quantitative quality metrics
- **Dynamic strategy:** Auto-select strategy based on task
- **Cost tracking:** Per-request cost monitoring
- **A/B testing:** Compare provider performance
- **Response synthesis:** Combine insights from multiple providers
- **Streaming support:** For compatible strategies
- **Custom scoring:** User-defined quality metrics

## Architecture

```
MixtureOfExpertsProvider
    ├── Strategy: voting
    │   └── Query all providers in parallel
    │       └── Use consensus/majority
    │
    ├── Strategy: cascade
    │   └── Try providers sequentially
    │       └── Return first success
    │
    ├── Strategy: task_based
    │   └── Analyze task keywords
    │       └── Route to best provider
    │
    ├── Strategy: best_of_n
    │   └── Query all providers
    │       └── Score and pick best
    │
    └── Strategy: specialist
        └── Route by operation type
            └── Specialized handling
```

## Conclusion

The MoE provider turns the Noseeum Agent Framework into a truly multi-model system, combining the strengths of Claude (reasoning), DeepSeek (code), and Mistral (creativity) into a unified "Frankenstein" ensemble.

Choose your strategy based on your priorities:
- **Speed + Cost:** task_based, specialist
- **Quality:** voting, best_of_n
- **Reliability:** cascade

Start with task_based and upgrade to voting for critical workflows!
