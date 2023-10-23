"""Stream type classes for tap-f1."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_f1.client import F1Stream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UsersStream(F1Stream):
    """Define custom stream."""

    name = "users"
    path = "/users"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "age",
            th.IntegerType,
            description="The user's age in years",
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address",
        ),
        th.Property("street", th.StringType),
        th.Property("city", th.StringType),
        th.Property(
            "state",
            th.StringType,
            description="State name in ISO 3166-2 format",
        ),
        th.Property("zip", th.StringType),
    ).to_dict()


class GroupsStream(F1Stream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
