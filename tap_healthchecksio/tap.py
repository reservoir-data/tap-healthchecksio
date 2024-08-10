"""Healthchecks.io tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_healthchecksio import streams


class TapHealthchecksIO(Tap):
    """Singer tap for Healthchecks.io."""

    name = "tap-healthchecksio"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API Key for Healthchecks.io",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Healthchecks.io streams.
        """
        return [streams.Checks(tap=self), streams.Flips(tap=self)]
