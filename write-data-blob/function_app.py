import azure.functions as func
import logging
from datetime import datetime

from helpers.azure_blob import AzBlobStorage
from helpers.leetcode import fetch_recent_submissions

blob_storage = AzBlobStorage("data")

app = func.FunctionApp()


@app.route(route="leetcode-write-data", methods=["GET"])
def leetcode_write_data(req: func.HttpRequest) -> func.HttpResponse:
    data = fetch_recent_submissions("username")
    blob_storage.write_json(f"lc-data-{datetime.now().strftime('%Y%m%d')}.json", data)

    logging.info("Python HTTP trigger function executed.")
    return func.HttpResponse("Leetcode summary executed successfully.", status_code=200)
