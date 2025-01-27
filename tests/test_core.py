"""Tests standard tap features using the built-in SDK tests library."""

from datetime import date

from singer_sdk.testing import get_tap_test_class

from tap_f1.tap import TapF1

SAMPLE_CONFIG = {
    "start_date": date(2024, 1, 1).isoformat(),
}


# Run standard built-in tap tests from the SDK:
TestTapF1 = get_tap_test_class(
    tap_class=TapF1,
    config=SAMPLE_CONFIG,
)
