import logging
import azure.functions as func
from helpers.leetcode import summary_lc

app = func.FunctionApp()


# @app.timer_trigger(
#     schedule="* 58 0 * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False
# )
# def leetcode_summary(myTimer: func.TimerRequest) -> None:
#     summary_lc()

#     logging.info("Python timer trigger function executed.")


@app.route(route="leetcode-post-summary", methods=["GET"])
def leetcode_post_summary(req: func.HttpRequest) -> func.HttpResponse:
    summary_lc()
    logging.info('Python HTTP trigger function executed.')
    return func.HttpResponse("Leetcode summary executed successfully.", status_code=200)
