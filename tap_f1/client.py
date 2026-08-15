# Copyright (c) 2026 Reuben Frankel.

"""REST client handling, including F1Stream base class."""

from datetime import date, timedelta
from functools import cached_property

from requests_cache import CachedSession
from singer_sdk.exceptions import ConfigValidationError
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_f1.pagination import F1Paginator


class F1Stream(RESTStream):
    """F1 stream class."""

    url_base = "https://api.jolpi.ca/ergast/f1"
    _limit = 100

    @override
    @cached_property
    def requests_session(self):
        session = CachedSession(
            self.tap_name,
            use_cache_dir=True,
            expire_after=timedelta(days=1),
        )
        # Pin Accept-Encoding so the Vary-based cache key stays stable across Python
        # versions. Python 3.14 bundles zstd in the standard library, so urllib3
        # advertises "gzip,deflate,zstd" instead of "gzip,deflate". Because the API
        # sends "Vary: Accept-Encoding", that mismatch makes 3.14 miss the shared
        # cache written by 3.10-3.13 and refetch every response from the upstream API.
        session.headers["Accept-Encoding"] = "gzip, deflate"
        return session

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

    @cached_property
    def end_date(self):
        """Get end date."""
        return date.fromisoformat(self.config["end_date"])

    def get_starting_date(self, context):
        """Get starting replication date."""
        start_value = self.get_starting_replication_key_value(context)
        start_date = date.fromisoformat(start_value)

        if start_date > self.end_date:
            msg = (
                "Start date cannot be greater than end date: "
                f"{start_date} > {self.end_date}"
            )
            raise ConfigValidationError(msg)

        return start_date
