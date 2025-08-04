import os
from pep440_version_utils import Version, is_valid_version


def compare_rasa_pro_versions() -> bool:
    """
    Compare the Pypi and the dispatched release versions for Rasa Pro.

    Returns:
        bool: True if an update is needed, False otherwise.
    """

    latest_pypi_image_version = os.getenv("LATEST_RASA_PRO_VERSION")
    dispatched_image_version = os.getenv("DISPATCHED_RASA_PRO_VERSION")

    if not latest_pypi_image_version or not dispatched_image_version:
        print(
            "Environment variables LATEST_RASA_PRO_VERSION and DISPATCHED_RASA_PRO_VERSION must be set."
        )
        return False

    if not is_valid_version(latest_pypi_image_version):
        print(f"Invalid pypi image tag: {latest_pypi_image_version}")
        return False

    if not is_valid_version(dispatched_image_version):
        print(f"Invalid dispatched release image tag: {dispatched_image_version}")
        return False

    latest_pypi_image_tag_version = Version(latest_image_version)
    dispatched_image_tag_version = Version(dispatched_image_version)

    return latest_pypi_image_tag_version == dispatched_image_tag_version


if __name__ == "__main__":
    if compare_rasa_pro_versions():
        print("true")
    else:
        print("false")
