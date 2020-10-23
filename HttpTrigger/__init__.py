import logging

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    response = requests.get("https://microsoft.com")
    return func.HttpResponse(
        f"Using requests module to get https://microsoft.com (status_code: {response.status_code})"
    )
