from singer_sdk.pagination import BaseOffsetPaginator


class F1Paginator(BaseOffsetPaginator):
    def has_more(self, response):
        data = response.json()["MRData"]

        limit = int(data["limit"])
        offset = int(data["offset"])
        total = int(data["total"])

        return (limit + offset) < total
