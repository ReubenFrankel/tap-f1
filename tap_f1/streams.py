"""Stream type classes for tap-f1."""


from singer_sdk import typing as th

from tap_f1.client import F1Stream


class SpeedUnitType(th.StringType):
    @th.DefaultInstanceProperty
    def type_dict(self):
        return {
            **super().type_dict,
            "enum": [
                "kph",
                "mph",
            ],
        }


class SeasonsStream(F1Stream):
    """Define seasons stream."""

    name = "seasons"
    primary_keys = ["season"]
    path = "/seasons.json"
    records_jsonpath = "MRData.SeasonTable.Seasons[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("url", th.URIType),
    ).to_dict()

    def get_child_context(self, record, context):
        return {"season": record["season"]}


class CircuitsStream(F1Stream):
    """Define circuits stream."""

    parent_stream_type = SeasonsStream
    name = "circuits"
    primary_keys = ["circuitId"]
    path = "/{season}/circuits.json"
    records_jsonpath = "MRData.CircuitTable.Circuits[*]"

    schema = th.PropertiesList(
        th.Property("circuitId", th.StringType),
        th.Property("url", th.URIType),
        th.Property("circuitName", th.StringType),
        th.Property(
            "Location",
            th.ObjectType(
                th.Property("lat", th.StringType),
                th.Property("long", th.StringType),
                th.Property("locality", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
    ).to_dict()


class DriversStream(F1Stream):
    """Define drivers stream."""

    parent_stream_type = SeasonsStream
    context_key = "Driver"
    name = "drivers"
    primary_keys = ["driverId"]
    path = "/{season}/drivers.json"
    records_jsonpath = "MRData.DriverTable.Drivers[*]"

    schema = th.PropertiesList(
        th.Property("driverId", th.StringType),
        th.Property("permanentNumber", th.StringType),
        th.Property("code", th.StringType),
        th.Property("url", th.URIType),
        th.Property("givenName", th.StringType),
        th.Property("familyName", th.StringType),
        th.Property("dateOfBirth", th.DateType),
        th.Property("nationality", th.StringType),
    ).to_dict()


class ConstructorsStream(F1Stream):
    """Define constructors stream."""

    parent_stream_type = SeasonsStream
    context_key = "Constructor"
    name = "constructors"
    primary_keys = ["constructorId"]
    path = "/{season}/constructors.json"
    records_jsonpath = "MRData.ConstructorTable.Constructors[*]"

    schema = th.PropertiesList(
        th.Property("constructorId", th.StringType),
        th.Property("url", th.URIType),
        th.Property("name", th.StringType),
        th.Property("nationality", th.StringType),
    ).to_dict()


class RacesStream(F1Stream):
    """Define races stream."""

    parent_stream_type = SeasonsStream
    name = "races"
    primary_keys = ["season", "round"]
    path = "/{season}.json"
    records_jsonpath = "MRData.RaceTable.Races[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("url", th.URIType),
        th.Property("raceName", th.StringType),
        th.Property(
            "Circuit",
            th.ObjectType(
                th.Property("circuitId", th.StringType),
                th.Property("url", th.URIType),
                th.Property("circuitName", th.StringType),
                th.Property(
                    "Location",
                    th.ObjectType(
                        th.Property("lat", th.StringType),
                        th.Property("long", th.StringType),
                        th.Property("locality", th.StringType),
                        th.Property("country", th.StringType),
                    ),
                ),
            ),
        ),
        th.Property("date", th.DateType),
        th.Property("time", th.StringType),
        th.Property(
            "FirstPractice",
            th.ObjectType(
                th.Property("date", th.DateType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "SecondPractice",
            th.ObjectType(
                th.Property("date", th.DateType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "ThirdPractice",
            th.ObjectType(
                th.Property("date", th.DateType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "Qualifying",
            th.ObjectType(
                th.Property("date", th.DateType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "Sprint",
            th.ObjectType(
                th.Property("date", th.DateType),
                th.Property("time", th.StringType),
            ),
        ),
    ).to_dict()

    def get_child_context(self, record, context):
        return {
            "season": record["season"],
            "round": record["round"],
        }


class QualifyingResultsStream(F1Stream):
    """Define qualifying results stream."""

    parent_stream_type = RacesStream
    name = "qualifying_results"
    primary_keys = ["season", "round", "number"]
    path = "/{season}/{round}/qualifying.json"
    records_jsonpath = "MRData.RaceTable.Races[*].QualifyingResults[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("number", th.StringType),
        th.Property("position", th.StringType),
        th.Property(
            "Driver",
            th.ObjectType(
                th.Property("driverId", th.StringType),
                th.Property("permanentNumber", th.StringType),
                th.Property("code", th.StringType),
                th.Property("url", th.URIType),
                th.Property("givenName", th.StringType),
                th.Property("familyName", th.StringType),
                th.Property("dateOfBirth", th.DateType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property(
            "Constructor",
            th.ObjectType(
                th.Property("constructorId", th.StringType),
                th.Property("url", th.URIType),
                th.Property("name", th.StringType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property("Q1", th.StringType),
        th.Property("Q2", th.StringType),
        th.Property("Q3", th.StringType),
    ).to_dict()


class SprintResultsStream(F1Stream):
    """Define sprint results stream."""

    parent_stream_type = RacesStream
    name = "sprints_results"
    primary_keys = ["season", "round", "number"]
    path = "/{season}/{round}/sprint.json"
    records_jsonpath = "MRData.RaceTable.Races[*].SprintResults[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("number", th.StringType),
        th.Property("position", th.StringType),
        th.Property("positionText", th.StringType),
        th.Property("points", th.StringType),
        th.Property(
            "Driver",
            th.ObjectType(
                th.Property("driverId", th.StringType),
                th.Property("permanentNumber", th.StringType),
                th.Property("code", th.StringType),
                th.Property("url", th.URIType),
                th.Property("givenName", th.StringType),
                th.Property("familyName", th.StringType),
                th.Property("dateOfBirth", th.DateType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property(
            "Constructor",
            th.ObjectType(
                th.Property("constructorId", th.StringType),
                th.Property("url", th.URIType),
                th.Property("name", th.StringType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property("grid", th.StringType),
        th.Property("laps", th.StringType),
        th.Property("status", th.StringType),
        th.Property(
            "Time",
            th.ObjectType(
                th.Property("millis", th.StringType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "FastestLap",
            th.ObjectType(
                th.Property("rank", th.StringType),
                th.Property("lap", th.StringType),
                th.Property(
                    "Time",
                    th.ObjectType(
                        th.Property("time", th.StringType),
                    ),
                ),
                th.Property(
                    "AverageSpeed",
                    th.ObjectType(
                        th.Property("units", SpeedUnitType),
                        th.Property("speed", th.StringType),
                    ),
                ),
            ),
        ),
    ).to_dict()


class RaceResultsStream(F1Stream):
    """Define race results stream."""

    parent_stream_type = RacesStream
    name = "race_results"
    primary_keys = ["season", "round", "number"]
    path = "/{season}/{round}/results.json"
    records_jsonpath = "MRData.RaceTable.Races[*].Results[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("number", th.StringType),
        th.Property("position", th.StringType),
        th.Property("positionText", th.StringType),
        th.Property("points", th.StringType),
        th.Property(
            "Driver",
            th.ObjectType(
                th.Property("driverId", th.StringType),
                th.Property("permanentNumber", th.StringType),
                th.Property("code", th.StringType),
                th.Property("url", th.URIType),
                th.Property("givenName", th.StringType),
                th.Property("familyName", th.StringType),
                th.Property("dateOfBirth", th.DateType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property(
            "Constructor",
            th.ObjectType(
                th.Property("constructorId", th.StringType),
                th.Property("url", th.URIType),
                th.Property("name", th.StringType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property("grid", th.StringType),
        th.Property("laps", th.StringType),
        th.Property("status", th.StringType),
        th.Property(
            "Time",
            th.ObjectType(
                th.Property("millis", th.StringType),
                th.Property("time", th.StringType),
            ),
        ),
        th.Property(
            "FastestLap",
            th.ObjectType(
                th.Property("rank", th.StringType),
                th.Property("lap", th.StringType),
                th.Property(
                    "Time",
                    th.ObjectType(
                        th.Property("time", th.StringType),
                    ),
                ),
                th.Property(
                    "AverageSpeed",
                    th.ObjectType(
                        th.Property("units", SpeedUnitType),
                        th.Property("speed", th.StringType),
                    ),
                ),
            ),
        ),
    ).to_dict()

    def get_child_context(self, record, context):
        return {
            **super().get_child_context(record, context),
            "driverId": record["Driver"]["driverId"],
        }


class LapsStream(F1Stream):
    """Define laps stream."""

    parent_stream_type = RaceResultsStream
    name = "laps"
    primary_keys = ["season", "round", "driverId", "number"]
    path = "/{season}/{round}/drivers/{driverId}/laps.json"
    records_jsonpath = "MRData.RaceTable.Races[*].Laps[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("driverId", th.StringType),
        th.Property("number", th.StringType),
        th.Property(
            "Timings",
            th.ArrayType(
                th.ObjectType(
                    th.Property("driverId", th.StringType),
                    th.Property("position", th.StringType),
                    th.Property("time", th.StringType),
                )
            ),
        ),
    ).to_dict()


class PitStopsStream(F1Stream):
    """Define pit stops stream."""

    parent_stream_type = RacesStream
    name = "pit_stops"
    primary_keys = ["season", "round", "driverId", "stop"]
    path = "/{season}/{round}/pitstops.json"
    records_jsonpath = "MRData.RaceTable.Races[*].PitStops[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("driverId", th.StringType),
        th.Property("lap", th.StringType),
        th.Property("stop", th.StringType),
        th.Property("time", th.TimeType),
        th.Property("duration", th.StringType),
    ).to_dict()


class DriverStandingsStream(F1Stream):
    """Define driver standings stream."""

    parent_stream_type = RacesStream
    name = "driver_standings"
    primary_keys = ["season", "round", "driverId", "position"]
    path = "/{season}/{round}/driverStandings.json"
    records_jsonpath = "MRData.StandingsTable.StandingsLists[*].DriverStandings[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("driverId", th.StringType),
        th.Property("position", th.StringType),
        th.Property("positionText", th.StringType),
        th.Property("points", th.StringType),
        th.Property("wins", th.StringType),
        th.Property(
            "Driver",
            th.ObjectType(
                th.Property("driverId", th.StringType),
                th.Property("permanentNumber", th.StringType),
                th.Property("code", th.StringType),
                th.Property("url", th.URIType),
                th.Property("givenName", th.StringType),
                th.Property("familyName", th.StringType),
                th.Property("dateOfBirth", th.DateType),
                th.Property("nationality", th.StringType),
            ),
        ),
        th.Property(
            "Constructors",
            th.ArrayType(
                th.ObjectType(
                    th.Property("constructorId", th.StringType),
                    th.Property("url", th.URIType),
                    th.Property("name", th.StringType),
                    th.Property("nationality", th.StringType),
                )
            ),
        ),
    ).to_dict()

    def post_process(self, row, context):
        # driverId forms part of primary key
        row["driverId"] = row["Driver"]["driverId"]

        return row


class ConstructorStandingsStream(F1Stream):
    """Define constructor standings stream."""

    parent_stream_type = RacesStream
    name = "constructor_standings"
    primary_keys = ["season", "round", "constructorId", "position"]
    path = "/{season}/{round}/constructorStandings.json"
    records_jsonpath = "MRData.StandingsTable.StandingsLists[*].ConstructorStandings[*]"

    schema = th.PropertiesList(
        th.Property("season", th.StringType),
        th.Property("round", th.StringType),
        th.Property("constructorId", th.StringType),
        th.Property("position", th.StringType),
        th.Property("positionText", th.StringType),
        th.Property("points", th.StringType),
        th.Property("wins", th.StringType),
        th.Property(
            "Constructor",
            th.ObjectType(
                th.Property("constructorId", th.StringType),
                th.Property("url", th.URIType),
                th.Property("name", th.StringType),
                th.Property("nationality", th.StringType),
            ),
        ),
    ).to_dict()

    def post_process(self, row, context):
        # constructorId forms part of primary key
        row["constructorId"] = row["Constructor"]["constructorId"]

        return row
