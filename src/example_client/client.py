"""Minimal async HTTP client skeleton."""

from __future__ import annotations

import logging
from typing import Any

from aiohttp import ClientSession

from .exceptions import AuthError, ClientError

_LOGGER = logging.getLogger(__name__)


class Client:
    """Async client.

    Parameters
    ----------
    session:
        Shared ``aiohttp.ClientSession`` (HA integrations should pass the one from
        ``async_get_clientsession(hass)``).
    base_url:
        API root without trailing slash.
    token:
        Optional bearer token; refresh ownership stays with the caller.
    """

    def __init__(
        self,
        session: ClientSession,
        *,
        base_url: str,
        token: str | None = None,
    ) -> None:
        self._session = session
        self._base_url = base_url.rstrip("/")
        self._token = token

    def set_token(self, token: str | None) -> None:
        """Update the bearer token after a refresh."""
        self._token = token

    async def async_get_json(self, path: str) -> dict[str, Any]:
        """GET JSON from ``path`` (must start with ``/``)."""
        headers: dict[str, str] = {}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        url = f"{self._base_url}{path}"
        try:
            async with self._session.get(url, headers=headers) as resp:
                if resp.status in (401, 403):
                    raise AuthError(f"Unauthorized ({resp.status})", code=str(resp.status))
                if resp.status >= 400:
                    body = await resp.text()
                    raise ClientError(f"HTTP {resp.status}: {body[:200]}", code=str(resp.status))
                data = await resp.json(content_type=None)
        except (AuthError, ClientError):
            raise
        except Exception as err:
            raise ClientError(f"Request failed: {err}") from err
        if not isinstance(data, dict):
            raise ClientError("Expected a JSON object response")
        return data
