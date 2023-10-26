"""F1 tap class."""

from singer_sdk import Tap

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

    def discover_streams(self):
        return [stream_type(self) for stream_type in STREAM_TYPES]


if __name__ == "__main__":
    TapF1.cli()
