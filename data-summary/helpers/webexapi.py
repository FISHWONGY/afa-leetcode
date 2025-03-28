import requests
from typing import Union

from settings import app_config


def post_to_webex(
    bearer_token: str,
    room_id: str,
    message: Union[str, dict],
    is_adaptive_card: bool = False,
):

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    if is_adaptive_card:
        payload = {
            "roomId": room_id,
            "markdown": "A markdown message.",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": message,
                }
            ],
        }
    else:
        payload = {"roomId": room_id, "markdown": message}

    requests.post(app_config.WEBEXAPI_URL, headers=headers, json=payload, timeout=60)
