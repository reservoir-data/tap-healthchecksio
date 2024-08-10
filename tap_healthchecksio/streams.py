"""Stream type classes for tap-healthchecksio."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th

from tap_healthchecksio.client import HealthchecksIOStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class Checks(HealthchecksIOStream):
    """Checks stream."""

    name = "checks"
    path = "/v3/checks/"
    primary_keys = ("unique_key",)
    replication_key = None

    records_jsonpath = "$.checks[*]"

    schema = th.PropertiesList(
        th.Property("unique_key", th.StringType),
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("tags", th.StringType),
        th.Property("desc", th.StringType),
        th.Property("grace", th.IntegerType),
        th.Property("n_pings", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("started", th.BooleanType),
        th.Property("last_ping", th.DateTimeType),
        th.Property("next_ping", th.DateTimeType),
        th.Property("manual_resume", th.BooleanType),
        th.Property("methods", th.StringType),
        th.Property("start_kw", th.StringType),
        th.Property("success_kw", th.StringType),
        th.Property("failure_kw", th.StringType),
        th.Property("filter_subject", th.BooleanType),
        th.Property("filter_body", th.BooleanType),
        th.Property("timeout", th.IntegerType),
    ).to_dict()

    def generate_child_contexts(
        self,
        record: dict[str, t.Any],
        context: Context | None,  # noqa: ARG002
    ) -> t.Iterable[Context | None]:
        """Generate child contexts for the record."""
        yield {"unique_key": record["unique_key"]}


class Flips(HealthchecksIOStream):
    """Flips stream."""

    name = "flips"
    path = "/v3/checks/{unique_key}/flips/"
    primary_keys = ("unique_key", "timestamp")
    replication_key = None

    parent_stream_type = Checks
    records_jsonpath = "$.flips[*]"

    schema = th.PropertiesList(
        th.Property("unique_key", th.StringType),
        th.Property("timestamp", th.StringType),
        th.Property("up", th.IntegerType),
    ).to_dict()
