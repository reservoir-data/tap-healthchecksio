"""REST client handling, including HealthchecksIOStream base class."""

from __future__ import annotations

from typing import Any, override

from singer_sdk import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator


class HealthchecksIOStream(RESTStream[Any]):
    """Healthchecks.io stream class."""

    url_base = "https://healthchecks.io/api"

    @override
    @property
    def authenticator(self) -> APIKeyAuthenticator:
        return APIKeyAuthenticator(
            key="x-api-key",
            value=self.config["api_key"],
            location="header",
        )
