"""Client unit tests."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from example_client import AuthError, Client, ClientError


def _mock_response(*, status: int = 200, json_data: dict | None = None, text: str = "") -> MagicMock:
    resp = MagicMock()
    resp.status = status
    resp.text = AsyncMock(return_value=text)
    resp.json = AsyncMock(return_value=json_data if json_data is not None else {})
    resp.__aenter__ = AsyncMock(return_value=resp)
    resp.__aexit__ = AsyncMock(return_value=None)
    return resp


@pytest.mark.asyncio
async def test_get_json_ok() -> None:
    session = MagicMock()
    session.get = MagicMock(return_value=_mock_response(json_data={"ok": True}))
    client = Client(session, base_url="https://api.example.com", token="good")
    data = await client.async_get_json("/v1/ping")
    assert data == {"ok": True}
    session.get.assert_called_once()
    _, kwargs = session.get.call_args
    assert kwargs["headers"]["Authorization"] == "Bearer good"


@pytest.mark.asyncio
async def test_get_json_auth_error() -> None:
    session = MagicMock()
    session.get = MagicMock(return_value=_mock_response(status=401, text="nope"))
    client = Client(session, base_url="https://api.example.com", token="bad")
    with pytest.raises(AuthError):
        await client.async_get_json("/v1/ping")


@pytest.mark.asyncio
async def test_get_json_client_error() -> None:
    session = MagicMock()
    session.get = MagicMock(return_value=_mock_response(status=500, text="boom"))
    client = Client(session, base_url="https://api.example.com")
    with pytest.raises(ClientError):
        await client.async_get_json("/v1/ping")
