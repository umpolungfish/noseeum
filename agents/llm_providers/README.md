# LLM Provider Abstraction Layer

Multi-provider LLM integration for the Noseeum Agent Framework. Supports Anthropic Claude, DeepSeek, and Mistral AI with a unified interface.

## Overview

The LLM Provider system allows agents to use different LLM providers interchangeably without changing agent code. All providers implement a common interface with standardized request/response formats.

## Supported Providers

| Provider | Status | API Type | Package Required |
|----------|--------|----------|------------------|
| **Anthropic Claude** | ✅ Ready | Native SDK | `anthropic>=0.40.0` |
| **DeepSeek** | ✅ Ready | HTTP (OpenAI-compatible) | `requests>=2.31.0` |
| **Mistral AI** | ✅ Ready | Native SDK | `mistralai>=1.0.0` |

## Quick Start

### 1. Set Environment Variables

```bash
# Set API key for your chosen provider
export ANTHROPIC_API_KEY="sk-ant-..."
export DEEPSEEK_API_KEY="sk-..."
export MISTRAL_API_KEY="..."
```

### 2. Configure Provider

Edit `agents/config.yaml`:

```yaml
llm_provider:
  provider: deepseek  # or: anthropic, mistral

  deepseek:
    api_key: ${DEEPSEEK_API_KEY}
    model: deepseek-chat
    max_tokens: 8000
```

### 3. Use in Agents

Agents automatically use the configured provider:

```python
from agents.base.agent import BaseAgent, AgentCapability

class MyAgent(BaseAgent):
    def run(self, task, context=None):
        self.start()

        # Recommended: Use provider-agnostic call_llm()
        messages = [{"role": "user", "content": task}]
        response = self.call_llm(messages, tools=self.get_tools())

        # Process response
        for block in response.content:
            if block["type"] == "text":
                print(block["text"])

        self.complete({"result": "success"})
        return {"status": "completed"}

    def get_tools(self):
        return self.toolkit.get_noseeum_tools()
```

## Provider Configuration

### Anthropic Claude

```yaml
llm_provider:
  provider: anthropic

  anthropic:
    api_key: ${ANTHROPIC_API_KEY}
    model: claude-sonnet-4-5-20250929  # or claude-opus-4-5-20251101
    max_tokens: 8000
    temperature: 0.7
```

**Models:**
- `claude-sonnet-4-5-20250929` - Fast, balanced (default)
- `claude-opus-4-5-20251101` - Most capable

**API Key:** Get from https://console.anthropic.com/

### DeepSeek

```yaml
llm_provider:
  provider: deepseek

  deepseek:
    api_key: ${DEEPSEEK_API_KEY}
    model: deepseek-chat
    max_tokens: 8000
    temperature: 0.7
    # base_url: "https://api.deepseek.com"  # Optional custom endpoint
```

**Models:**
- `deepseek-chat` - General purpose (default)
- `deepseek-coder` - Optimized for code

**API Key:** Get from https://platform.deepseek.com/

### Mistral AI

```yaml
llm_provider:
  provider: mistral

  mistral:
    api_key: ${MISTRAL_API_KEY}
    model: mistral-large-latest
    max_tokens: 8000
    temperature: 0.7
```

**Models:**
- `mistral-large-latest` - Most capable (default)
- `mistral-medium-latest` - Balanced performance
- `mistral-small-latest` - Fast, cost-effective

**API Key:** Get from https://console.mistral.ai/

## Per-Agent Provider Override

Override the provider for specific agents:

```yaml
agents:
  unicode_archaeologist:
    enabled: true
    llm_provider: deepseek  # Use DeepSeek for this agent
    model: deepseek-chat

  payload_artisan:
    enabled: true
    llm_provider: mistral   # Use Mistral for this agent
    model: mistral-large-latest
```

## API Reference

### LLMProvider Interface

All providers implement this interface:

```python
class LLMProvider(ABC):
    @abstractmethod
    def create_completion(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        max_tokens: int = 4000,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """Create a completion."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if provider is available."""
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """Get provider name."""
        pass
```

### LLMResponse Object

Standardized response format:

```python
@dataclass
class LLMResponse:
    content: List[Dict[str, Any]]  # Content blocks
    stop_reason: str               # "end_turn", "tool_use", "max_tokens"
    usage: Dict[str, int]          # Token usage
    model: str                     # Model used
    raw_response: Any              # Original response
```

### Tool Schema Format

Tools use Anthropic format (automatically converted for other providers):

```python
tool = {
    "name": "search_code",
    "description": "Search for code patterns",
    "input_schema": {
        "type": "object",
        "properties": {
            "pattern": {"type": "string", "description": "Regex pattern"},
            "directory": {"type": "string", "description": "Directory to search"}
        },
        "required": ["pattern"]
    }
}
```

## Usage Examples

### Basic Usage

```python
from agents.llm_providers import LLMProviderFactory

# Create provider
provider = LLMProviderFactory.create_provider("deepseek")

# Make API call
response = provider.create_completion(
    messages=[{"role": "user", "content": "Hello!"}]
)

# Process response
for block in response.content:
    if block["type"] == "text":
        print(block["text"])
```

### With Tool Calling

```python
# Define tools
tools = [
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
]

# Make call with tools
response = provider.create_completion(
    messages=[{"role": "user", "content": "What's the weather in SF?"}],
    tools=tools
)

# Check for tool calls
for block in response.content:
    if block["type"] == "tool_use":
        print(f"Tool: {block['name']}")
        print(f"Input: {block['input']}")
```

### Provider Comparison

```python
from agents.llm_providers import LLMProviderFactory

providers = ["anthropic", "deepseek", "mistral"]
messages = [{"role": "user", "content": "Explain recursion"}]

for provider_name in providers:
    provider = LLMProviderFactory.create_provider(provider_name)

    if provider.is_available():
        response = provider.create_completion(messages)
        print(f"\n{provider_name}:")
        print(f"Tokens: {response.usage['total_tokens']}")
        print(f"Response: {response.content[0]['text'][:100]}...")
```

### Dynamic Provider Selection

```python
def select_provider(task: str) -> str:
    """Select best provider for task."""
    if "code" in task.lower():
        return "deepseek"  # DeepSeek good for code
    elif "creative" in task.lower():
        return "mistral"   # Mistral good for creative tasks
    else:
        return "anthropic" # Claude default

# Use selected provider
provider_name = select_provider("Write a Python function")
provider = LLMProviderFactory.create_provider(provider_name)
response = provider.create_completion(messages)
```

## Tool Schema Conversion

### Anthropic Format (Base)

```json
{
  "name": "file_read",
  "description": "Read file contents",
  "input_schema": {
    "type": "object",
    "properties": {
      "filepath": {"type": "string"}
    },
    "required": ["filepath"]
  }
}
```

### OpenAI Format (DeepSeek)

Automatically converted to:

```json
{
  "type": "function",
  "function": {
    "name": "file_read",
    "description": "Read file contents",
    "parameters": {
      "type": "object",
      "properties": {
        "filepath": {"type": "string"}
      },
      "required": ["filepath"]
    }
  }
}
```

## Backward Compatibility

### Old Code (Still Works)

```python
# Old method - still supported
response = self.call_claude(messages, tools)
# Returns provider-specific raw response
```

### New Code (Recommended)

```python
# New method - provider-agnostic
response = self.call_llm(messages, tools)
# Returns standardized LLMResponse object
```

## Error Handling

```python
try:
    response = provider.create_completion(messages)
except Exception as e:
    print(f"Provider error: {e}")
    # Fall back to another provider
    fallback = LLMProviderFactory.create_provider("anthropic")
    response = fallback.create_completion(messages)
```

## Demo Mode

When no API key is present, providers operate in demo mode:

```python
provider = LLMProviderFactory.create_provider("deepseek", api_key=None)
print(provider.is_available())  # False

response = provider.create_completion(messages)
print(response.content[0]["text"])  # "Demo mode - DeepSeek API key not set"
```

## Troubleshooting

### Provider Not Available

**Problem:** `provider.is_available()` returns `False`

**Solutions:**
1. Check API key is set: `echo $DEEPSEEK_API_KEY`
2. Set in config: `api_key: "sk-..."`
3. Check package installed: `pip list | grep mistralai`

### Mistral Import Error

**Problem:** `mistralai package not installed`

**Solution:**
```bash
pip install mistralai>=1.0.0
```

### Tool Calling Not Working

**Problem:** Tools not being used by provider

**Solutions:**
1. Check tool schema format (should be Anthropic format)
2. Verify provider supports tools (all 3 do)
3. Check model supports tools (some older models don't)

### Different Response Formats

**Problem:** Code expects Anthropic response format

**Solution:** Use `call_llm()` instead of `call_claude()`:

```python
# Old (provider-specific)
response = self.call_claude(messages, tools)
text = response.content[0].text  # Anthropic format

# New (standardized)
response = self.call_llm(messages, tools)
text = response.content[0]["text"]  # Works for all providers
```

## Architecture

```
BaseAgent
    ├── call_llm() [new, provider-agnostic]
    └── call_claude() [legacy, backward compatible]
         ↓
   LLMProviderFactory
         ↓
    ┌────┴────┬────────┐
Anthropic  DeepSeek  Mistral
Provider   Provider  Provider
    ↓          ↓         ↓
Anthropic  OpenAI   Mistral
   SDK      HTTP      SDK
```

## Contributing

### Adding a New Provider

1. Create `agents/llm_providers/newprovider_provider.py`:

```python
from .base_provider import LLMProvider, LLMResponse

class NewProviderProvider(LLMProvider):
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    def create_completion(self, messages, tools=None, **kwargs):
        # Implementation
        pass

    def is_available(self):
        return bool(self.api_key)

    def get_provider_name(self):
        return "newprovider"
```

2. Add to factory in `factory.py`:

```python
elif provider_name == "newprovider":
    return NewProviderProvider(api_key=api_key, model=model)
```

3. Update `__init__.py` exports

4. Add config in `config_sample.yaml`

5. Update `requirements.txt` if needed

## License

Part of the Noseeum Agent Framework.
