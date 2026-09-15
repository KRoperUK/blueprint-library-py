"""Public exception hierarchy.

Keep a small, stable set of exceptions the Home Assistant integration can map to
ConfigEntryAuthFailed / UpdateFailed / HomeAssistantError without importing HA here.
"""

from __future__ import annotations


class ClientError(Exception):
    """Base error for the client library."""

    def __init__(self, message: str, *, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class AuthError(ClientError):
    """Credentials are invalid or expired — caller should re-authenticate."""
