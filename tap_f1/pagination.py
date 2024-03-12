"""Pagination classes for tap-f1."""

from singer_sdk.pagination import BaseOffsetPaginator
from typing_extensions import override


class F1Paginator(BaseOffsetPaginator):
    """Base API paginator."""

    @override
    def has_more(self, response):
        data = response.json()["MRData"]

        limit = int(data["limit"])
        offset = int(data["offset"])
        total = int(data["total"])

        return (limit + offset) < total
