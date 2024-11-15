"""REST client handling, including F1Stream base class."""

from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_f1.pagination import F1Paginator


class F1Stream(RESTStream):
    """F1 stream class."""

    url_base = "https://api.jolpi.ca/ergast/f1"
    _limit = 1000

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
