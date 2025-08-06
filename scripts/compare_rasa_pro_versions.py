import os
from pep440_version_utils import Version, is_valid_version


def compare_rasa_pro_versions() -> bool:
    """
    Compare the Pypi and the dispatched release versions for Rasa Pro.

    Returns:
        bool: True if an update is needed, False otherwise.
    """

    latest_pypi_version = os.getenv("LATEST_RASA_PRO_VERSION")
    dispatched_version = os.getenv("DISPATCHED_RASA_PRO_VERSION")

    if not latest_pypi_version or not dispatched_version:
        print(
            "Environment variables LATEST_RASA_PRO_VERSION and DISPATCHED_RASA_PRO_VERSION must be set."
        )
        return False

    if not is_valid_version(latest_pypi_version):
        print(f"Invalid pypi version : {latest_pypi_version}")
        return False

    if not is_valid_version(dispatched_version):
        print(f"Invalid dispatched release version: {dispatched_version}")
        return False

    return Version(latest_pypi_version) == Version(dispatched_version)


if __name__ == "__main__":
    if compare_rasa_pro_versions():
        print("true")
    else:
        print("false")
