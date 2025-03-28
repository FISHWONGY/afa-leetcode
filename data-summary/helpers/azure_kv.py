from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging


logger = logging.getLogger("azure")
logger.setLevel(logging.INFO)


class AzKeyVault:
    def __init__(self) -> None:
        self.credential = DefaultAzureCredential()
        self.key_vault_url = f"https://my-app.vault.azure.net/"
        self.client = SecretClient(
            vault_url=self.key_vault_url,
            credential=self.credential,
            logging_enable=True,
        )

    def get_secret(self, secret: str):
        secret_response = self.client.get_secret(secret)
        creds = secret_response.value
        return creds
