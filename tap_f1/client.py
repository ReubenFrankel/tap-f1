"""REST client handling, including F1Stream base class."""

from datetime import date, timedelta

from requests_cache import CachedSession
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_f1.pagination import F1Paginator


class F1Stream(RESTStream):
    """F1 stream class."""

    url_base = "https://api.jolpi.ca/ergast/f1"
    _limit = 100

    def __init__(self, *args, **kwargs) -> None:
        """Initialise the F1 stream."""
        super().__init__(*args, **kwargs)
        self._requests_session = CachedSession(
            self.tap_name,
            use_cache_dir=True,
            expire_after=timedelta(days=1),
        )

    @override
    def get_new_paginator(self):
        return F1Paginator(0, self._limit)

    @override
    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        params["limit"] = self._limit

        if next_page_token:
            params["offset"] = next_page_token

        return params

    def get_starting_date(self, context):
        """Get starting replication date."""
        start_value = self.get_starting_replication_key_value(context)
        return date.fromisoformat(start_value)
