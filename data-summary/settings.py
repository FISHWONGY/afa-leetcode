from pydantic_settings import BaseSettings
from helpers.azure_kv import AzKeyVault

secrets = AzKeyVault()


class AppConfig(BaseSettings):
    """App Settins"""

    WEBEXAPI_URL: str = "https://api.ciscospark.com/v1/messages"
    LC_GRAPHQL_URL: str = "https://leetcode.com/graphql"

    LC_USERNAME: str = secrets.get_secret("username")
    BOT_TOKEN: str = secrets.get_secret("bot-token")
    ROOM_ID: str = secrets.get_secret("room-id")


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
