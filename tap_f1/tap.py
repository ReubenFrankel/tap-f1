"""F1 tap class."""

from datetime import date, datetime, timezone

import singer_sdk.typing as th
from singer_sdk import Tap
from typing_extensions import override

from tap_f1 import streams

STREAM_TYPES = [
    streams.SeasonsStream,
    streams.RacesStream,
    streams.CircuitsStream,
    streams.QualifyingResultsStream,
    streams.SprintResultsStream,
    streams.RaceResultsStream,
    streams.DriversStream,
    streams.ConstructorsStream,
    streams.LapsStream,
    streams.PitStopsStream,
    streams.DriverStandingsStream,
    streams.ConstructorStandingsStream,
]


class TapF1(Tap):
    """F1 tap class."""

    name = "tap-f1"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateType,
            default=date(datetime.now(tz=timezone.utc).year, 1, 1).isoformat(),
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [stream_type(self) for stream_type in STREAM_TYPES]


if __name__ == "__main__":
    TapF1.cli()
