# Copyright (c) 2026 Reuben Frankel.

"""Pagination classes for tap-f1."""

from singer_sdk.pagination import OffsetPaginator
from typing_extensions import override


class F1Paginator(OffsetPaginator):
    """Base API paginator."""

    @override
    def has_more(self, response):
        data = response.json()["MRData"]

        limit = int(data["limit"])
        offset = int(data["offset"])
        total = int(data["total"])

        return (limit + offset) < total
