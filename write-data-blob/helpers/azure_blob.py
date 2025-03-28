from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.identity import DefaultAzureCredential
import json
import logging

from settings import app_config

logger = logging.getLogger("azure")
logger.setLevel(logging.INFO)


class AzBlobStorage:
    def __init__(self, container_name: str) -> None:
        self.blob_service_client = BlobServiceClient.from_connection_string(
            app_config.AZURE_BLOB_CONNECTION_STRING
        )
        self.container_client = self.blob_service_client.get_container_client(
            container_name
        )

    def read_json(self, blob_name: str) -> dict:
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_data = blob_client.download_blob().readall()
            return json.loads(blob_data)
        except Exception as e:
            logger.error(f"Error reading blob {blob_name}: {e}")
            raise

    def write_json(self, blob_name: str, data: dict):
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_data = json.dumps(data)
            blob_client.upload_blob(blob_data, overwrite=True)
            logger.info(f"Successfully wrote to blob {blob_name}")
        except Exception as e:
            logger.error(f"Error writing to blob {blob_name}: {e}")
            raise
