from pydantic_settings import BaseSettings
from helpers.azure_kv import AzKeyVault

secrets = AzKeyVault()


class AppConfig(BaseSettings):
    """App Settins"""

    LC_GRAPHQL_URL: str = "https://leetcode.com/graphql"
    AZURE_STORAGE_ACCOUNT: str = "https://myrsrcgrp.blob.core.windows.net"
    AZURE_BLOB_CONNECTION_STRING: str = secrets.get_secret("blob-access-key")

    LC_USERNAME: str = secrets.get_secret("username")


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
