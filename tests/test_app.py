import aiohttp
import pytest
from aioresponses import aioresponses

from app import get_json

@pytest.mark.asyncio
async def test_get_json_failure():
    url = "https://jsonplaceholder.typicode.com/todos/invalid"

    with aioresponses() as mocked_responses:
        mocked_responses.get(url, exception=aiohttp.ClientResponseError(None, None, status=404))

        with pytest.raises(aiohttp.ClientResponseError) as exc_info:
            await get_json(url)

        assert exc_info.value.status == 404
