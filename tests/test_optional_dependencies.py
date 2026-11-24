import subprocess
import sys


def test_core_package_import_does_not_load_polars() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "import sys; "
                "from order_matching.matching_engine import MatchingEngine; "
                "assert 'polars' not in sys.modules; "
                "MatchingEngine()"
            ),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
