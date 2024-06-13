import contextlib
from functools import cache

import httpx
from pydantic import TypeAdapter

from models import ReportType, Unit

__all__ = ('UnitsStorageConnection', 'closing_units_storage_http_client')


@contextlib.asynccontextmanager
async def closing_units_storage_http_client(
        base_url: str,
) -> httpx.AsyncClient:
    async with httpx.AsyncClient(base_url=base_url) as http_client:
        yield http_client


class UnitsStorageConnection:

    def __init__(self, http_client: httpx.AsyncClient):
        self.__http_client = http_client

    # Units will change rarely.
    # In order to update the cache, you need to restart the application
    @cache
    async def get_units(self) -> list[Unit]:
        url = '/units/'
        response = await self.__http_client.get(url)
        response_data = response.json()['units']
        type_adapter = TypeAdapter(list[Unit])
        return type_adapter.validate_python(response_data)

    @cache  # Report types will never change
    async def get_report_type_by_name(self, name: str) -> ReportType:
        url = f'/report-types/names/{name}/'
        response = await self.__http_client.get(url)
        response_data = response.json()
        return ReportType.model_validate(response_data)

    async def get_routes_telegram_chat_ids(
            self,
            *,
            unit_id: int,
            report_type_id: int,
    ) -> set[int]:
        url = f'/report-routes/telegram-chats/'
        request_query_params = {
            'unit_id': unit_id,
            'report_type_id': report_type_id,
        }
        response = await self.__http_client.get(
            url=url,
            params=request_query_params,
        )
        return response.json()['chat_ids']
