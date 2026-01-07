"""Agent memory system for persistent storage and retrieval."""

import json
import os
from typing import Dict, Any, Optional, List
from datetime import datetime


class AgentMemory:
    """Persistent memory for agents."""

    def __init__(self, agent_id: str):
        """Initialize agent memory."""
        self.agent_id = agent_id
        self.memory_dir = f"agents/memory/{agent_id}"
        self.memory_file = f"{self.memory_dir}/memory.json"
        self._ensure_memory_dir()
        self.data = self._load_memory()

    def _ensure_memory_dir(self):
        """Ensure memory directory exists."""
        os.makedirs(self.memory_dir, exist_ok=True)

    def _load_memory(self) -> Dict[str, Any]:
        """Load memory from disk."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {
            "agent_id": self.agent_id,
            "created_at": datetime.now().isoformat(),
            "entries": {},
            "sessions": []
        }

    def save(self):
        """Save memory to disk."""
        self.data["updated_at"] = datetime.now().isoformat()
        with open(self.memory_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def store(self, key: str, value: Any, category: str = "general"):
        """Store data in memory."""
        if category not in self.data["entries"]:
            self.data["entries"][category] = {}

        self.data["entries"][category][key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
        self.save()

    def retrieve(self, key: str, category: str = "general") -> Optional[Any]:
        """Retrieve data from memory."""
        try:
            return self.data["entries"][category][key]["value"]
        except KeyError:
            return None

    def list_categories(self) -> List[str]:
        """List all memory categories."""
        return list(self.data["entries"].keys())

    def list_keys(self, category: str = "general") -> List[str]:
        """List all keys in a category."""
        if category in self.data["entries"]:
            return list(self.data["entries"][category].keys())
        return []

    def start_session(self, task: str) -> str:
        """Start a new session."""
        session_id = f"session_{len(self.data['sessions'])}"
        session = {
            "session_id": session_id,
            "task": task,
            "start_time": datetime.now().isoformat(),
            "events": []
        }
        self.data["sessions"].append(session)
        self.save()
        return session_id

    def log_event(self, session_id: str, event: str, data: Optional[Dict[str, Any]] = None):
        """Log an event to a session."""
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                session["events"].append({
                    "timestamp": datetime.now().isoformat(),
                    "event": event,
                    "data": data
                })
                self.save()
                break

    def end_session(self, session_id: str, result: Dict[str, Any]):
        """End a session."""
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                session["end_time"] = datetime.now().isoformat()
                session["result"] = result
                self.save()
                break

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get session data."""
        for session in self.data["sessions"]:
            if session["session_id"] == session_id:
                return session
        return None

    def clear_category(self, category: str):
        """Clear all data in a category."""
        if category in self.data["entries"]:
            del self.data["entries"][category]
            self.save()

    def clear_all(self):
        """Clear all memory."""
        self.data = {
            "agent_id": self.agent_id,
            "created_at": datetime.now().isoformat(),
            "entries": {},
            "sessions": []
        }
        self.save()
