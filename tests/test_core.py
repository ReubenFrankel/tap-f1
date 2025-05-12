"""Tests standard tap features using the built-in SDK tests library."""

from datetime import date

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_f1.tap import TapF1, streams

SAMPLE_CONFIG = {
    "start_date": date(2025, 1, 1).isoformat(),
}


# Run standard built-in tap tests from the SDK:
TestTapF1 = get_tap_test_class(
    tap_class=TapF1,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        ignore_no_records_for_streams=[streams.SprintResultsStream.name],
        max_records_limit=None,
    ),
)
