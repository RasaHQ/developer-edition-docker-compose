import os
import sys
from typing import Optional
from pep440_version_utils import Version, is_valid_version

RASA_PRO_IMAGE_TAG = "europe-west3-docker.pkg.dev/rasa-releases/rasa-pro/rasa-pro"
DEFAULT_RESPONSE = "No updates."


def update_rasa_pro_image_tag(
    latest_image_tag: str,
    current_image_tag: str,
) -> Optional[str]:
    """
    Update the Rasa Pro image tag to the latest version if the provided tag is valid.

    Args:
        latest_image_tag: The latest version of the Rasa Pro image.
        current_image_tag (str): The current image tag.

    Returns:
        str: The updated image tag if valid, otherwise the original tag.
    """
    if not is_valid_version(latest_image_tag):
        print(f"Invalid new image tag: {latest_image_tag}")
        sys.exit(1)

    if not is_valid_version(current_image_tag):
        print(f"Invalid current image tag: {current_image_tag}")
        sys.exit(1)

    latest_image_tag_version = Version(latest_image_tag)
    current_image_tag_version = Version(current_image_tag)

    if latest_image_tag_version <= current_image_tag_version:
        print(f"Keeping current Rasa Pro image tag: {current_image_tag}")
        return None

    return latest_image_tag


if __name__ == "__main__":
    latest_image_version = os.getenv("LATEST_RASA_PRO_VERSION")
    current_image_version = os.getenv("CURRENT_RASA_PRO_VERSION")

    if not latest_image_version or not current_image_version:
        print(
            "Environment variables LATEST_RASA_PRO_VERSION and CURRENT_RASA_PRO_VERSION must be set."
        )
        sys.exit(1)

    updated_tag = update_rasa_pro_image_tag(latest_image_version, current_image_version)
    if updated_tag:
        print(f"{updated_tag}")
    else:
        print(DEFAULT_RESPONSE)
        sys.exit(0)
