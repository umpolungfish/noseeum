"""Agent communication system for inter-agent messaging."""

import json
import os
import asyncio
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum
from queue import Queue, Empty


class MessageType(Enum):
    """Standardized message types for inter-agent communication."""
    REQUEST = "request"
    RESPONSE = "response"
    NOTIFICATION = "notification"
    COLLABORATION = "collaboration_request"


@dataclass
class Message:
    """Typed message container for inter-agent communication (AjintK pattern)."""
    message_id: str
    from_agent: str
    to_agent: str
    message_type: MessageType
    content: str
    priority: int = 5
    timestamp: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["message_type"] = self.message_type.value
        return d


class AgentCommunication:
    """Inter-agent communication system."""

    def __init__(self, agent_id: str):
        """Initialize communication system."""
        self.agent_id = agent_id
        self.comm_dir = "agents/communication"
        self.inbox_file = f"{self.comm_dir}/{agent_id}_inbox.json"
        self.outbox_file = f"{self.comm_dir}/{agent_id}_outbox.json"
        self.message_queue = Queue()
        self._lock = asyncio.Lock()
        self._ensure_comm_dir()

    def _ensure_comm_dir(self):
        """Ensure communication directory exists."""
        os.makedirs(self.comm_dir, exist_ok=True)

    def send_message(self, to_agent: str, message_type: str,
                     content: Dict[str, Any], priority: int = 5) -> str:
        """
        Send message to another agent.

        Args:
            to_agent: Target agent ID
            message_type: Type of message (request, response, notification, etc.)
            content: Message content
            priority: Message priority (1-10, 10 is highest)

        Returns:
            Message ID
        """
        message_id = f"{self.agent_id}_{to_agent}_{datetime.now().timestamp()}"
        message = {
            "message_id": message_id,
            "from": self.agent_id,
            "to": to_agent,
            "type": message_type,
            "content": content,
            "priority": priority,
            "timestamp": datetime.now().isoformat(),
            "status": "sent"
        }

        # Write to outbox
        self._write_to_outbox(message)

        # Write to recipient's inbox
        recipient_inbox = f"{self.comm_dir}/{to_agent}_inbox.json"
        self._append_to_file(recipient_inbox, message)

        return message_id

    def receive_messages(self, message_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Receive messages from inbox.

        Args:
            message_type: Optional filter by message type

        Returns:
            List of messages
        """
        if not os.path.exists(self.inbox_file):
            return []

        try:
            with open(self.inbox_file, 'r') as f:
                inbox = json.load(f)

            messages = inbox.get("messages", [])

            # Filter by type if specified
            if message_type:
                messages = [m for m in messages if m.get("type") == message_type]

            # Sort by priority and timestamp
            messages.sort(key=lambda m: (-m.get("priority", 5), m.get("timestamp", "")))

            return messages
        except:
            return []

    def mark_message_read(self, message_id: str):
        """Mark a message as read."""
        if not os.path.exists(self.inbox_file):
            return

        try:
            with open(self.inbox_file, 'r') as f:
                inbox = json.load(f)

            for message in inbox.get("messages", []):
                if message.get("message_id") == message_id:
                    message["status"] = "read"
                    message["read_at"] = datetime.now().isoformat()

            with open(self.inbox_file, 'w') as f:
                json.dump(inbox, f, indent=2)
        except:
            pass

    def broadcast(self, message_type: str, content: Dict[str, Any],
                  target_agents: Optional[List[str]] = None) -> List[str]:
        """
        Broadcast message to multiple agents.

        Args:
            message_type: Type of message
            content: Message content
            target_agents: Optional list of target agents (None = all)

        Returns:
            List of message IDs
        """
        message_ids = []

        if target_agents is None:
            # Get all agent inboxes
            target_agents = []
            for filename in os.listdir(self.comm_dir):
                if filename.endswith("_inbox.json"):
                    agent_id = filename.replace("_inbox.json", "")
                    if agent_id != self.agent_id:
                        target_agents.append(agent_id)

        for agent_id in target_agents:
            msg_id = self.send_message(agent_id, message_type, content)
            message_ids.append(msg_id)

        return message_ids

    def request_collaboration(self, target_agent: str, task: str,
                              context: Dict[str, Any]) -> str:
        """
        Request collaboration from another agent.

        Args:
            target_agent: Agent to collaborate with
            task: Task description
            context: Task context

        Returns:
            Request message ID
        """
        content = {
            "task": task,
            "context": context,
            "requesting_agent": self.agent_id
        }
        return self.send_message(target_agent, "collaboration_request", content, priority=8)

    def respond_to_request(self, message_id: str, response: Dict[str, Any]):
        """Respond to a collaboration request."""
        # Find the original message
        messages = self.receive_messages("collaboration_request")
        for msg in messages:
            if msg.get("message_id") == message_id:
                from_agent = msg.get("from")
                content = {
                    "original_message_id": message_id,
                    "response": response
                }
                self.send_message(from_agent, "collaboration_response", content, priority=8)
                self.mark_message_read(message_id)
                break

    def _write_to_outbox(self, message: Dict[str, Any]):
        """Write message to outbox (atomic write)."""
        outbox = {"messages": []}
        if os.path.exists(self.outbox_file):
            try:
                with open(self.outbox_file, 'r') as f:
                    outbox = json.load(f)
            except:
                pass

        outbox["messages"].append(message)

        temp_file = f"{self.outbox_file}.tmp"
        with open(temp_file, 'w') as f:
            json.dump(outbox, f, indent=2)
        os.replace(temp_file, self.outbox_file)

    def _append_to_file(self, filepath: str, message: Dict[str, Any]):
        """Append message to a file (atomic write)."""
        data = {"messages": []}
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
            except:
                pass

        data["messages"].append(message)

        temp_file = f"{filepath}.tmp"
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=2)
        os.replace(temp_file, filepath)

    # ------------------------------------------------------------------
    # Async message passing (AjintK pattern)
    # ------------------------------------------------------------------

    async def send_message_async(
        self,
        to_agent: str,
        message_type: MessageType,
        content: str,
        priority: int = 5,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Async variant of send_message() using the typed Message dataclass.
        Uses asyncio.Lock + asyncio.to_thread for non-blocking file I/O.
        """
        message_id = f"{self.agent_id}_{to_agent}_{datetime.now().timestamp()}"
        msg = Message(
            message_id=message_id,
            from_agent=self.agent_id,
            to_agent=to_agent,
            message_type=message_type,
            content=content,
            priority=priority,
            metadata=metadata,
        )
        msg_dict = msg.to_dict()

        async with self._lock:
            await asyncio.to_thread(self._write_to_outbox, msg_dict)
            if to_agent != "broadcast":
                inbox_path = f"{self.comm_dir}/{to_agent}_inbox.json"
                await asyncio.to_thread(self._append_to_file, inbox_path, msg_dict)

        return message_id

    async def receive_messages_async(
        self, unread_only: bool = True
    ) -> List[Dict[str, Any]]:
        """Async variant of receive_messages() with priority sorting."""
        if not os.path.exists(self.inbox_file):
            return []

        def _load():
            try:
                with open(self.inbox_file, 'r') as f:
                    inbox = json.load(f)
                return inbox.get("messages", [])
            except Exception:
                return []

        messages = await asyncio.to_thread(_load)

        if unread_only:
            messages = [m for m in messages if m.get("status") != "read"]

        messages.sort(key=lambda m: (-m.get("priority", 5), m.get("timestamp", "")))
        return messages

    async def mark_as_read_async(self, message_id: str) -> bool:
        """Async variant of mark_message_read()."""
        if not os.path.exists(self.inbox_file):
            return False

        async with self._lock:
            def _update():
                try:
                    with open(self.inbox_file, 'r') as f:
                        inbox = json.load(f)
                    for msg in inbox.get("messages", []):
                        if msg.get("message_id") == message_id:
                            msg["status"] = "read"
                            msg["read_at"] = datetime.now().isoformat()
                            temp = f"{self.inbox_file}.tmp"
                            with open(temp, 'w') as f:
                                json.dump(inbox, f, indent=2)
                            os.replace(temp, self.inbox_file)
                            return True
                except Exception:
                    pass
                return False

            return await asyncio.to_thread(_update)

    async def send_collaboration_request_async(
        self,
        target_agent: str,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Send a structured collaboration request asynchronously."""
        import json as _json
        metadata = {"task": task, "context": context or {}}
        content = _json.dumps({"task": task, "requesting_agent": self.agent_id})
        return await self.send_message_async(
            to_agent=target_agent,
            message_type=MessageType.COLLABORATION,
            content=content,
            priority=8,
            metadata=metadata,
        )

    async def send_response_async(
        self,
        to_agent: str,
        original_message_id: str,
        response_content: str,
        response_data: Optional[Dict[str, Any]] = None
    ) -> str:
        """Send a response to a prior message asynchronously."""
        metadata = {
            "in_response_to": original_message_id,
            "response_data": response_data or {},
        }
        return await self.send_message_async(
            to_agent=to_agent,
            message_type=MessageType.RESPONSE,
            content=response_content,
            priority=6,
            metadata=metadata,
        )

    def clear_inbox(self):
        """Clear all messages from inbox."""
        if os.path.exists(self.inbox_file):
            os.remove(self.inbox_file)

    def get_unread_count(self) -> int:
        """Get count of unread messages."""
        messages = self.receive_messages()
        return len([m for m in messages if m.get("status") != "read"])
