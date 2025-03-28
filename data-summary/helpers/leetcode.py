import requests
from datetime import datetime

from settings import app_config
from helpers.webexapi import post_to_webex


def fetch_recent_submissions(username, limit=30):
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id
        title
        titleSlug
        timestamp
      }
    }
    """

    variables = {"username": username, "limit": limit}

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        app_config.LC_GRAPHQL_URL,
        json={"query": query, "variables": variables},
        headers=headers,
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Query failed with status code {response.status_code}: {response.text}"
        )


def count_submissions_on_date(submissions, target_date):
    count = 0
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
    question_titles = []

    for submission in submissions:
        submission_date = datetime.fromtimestamp(int(submission["timestamp"])).date()
        if submission_date == target_date:
            count += 1
            question_titles.append(submission["title"])

    return count, question_titles


def summary_lc():
    target_date = datetime.now().strftime("%Y-%m-%d")
    data = fetch_recent_submissions(app_config.LC_USERNAME)
    submissions = data.get("data", {}).get("recentAcSubmissionList", [])
    count, question_titles = count_submissions_on_date(submissions, target_date)

    if question_titles:
        final_str = f"<blockquote class=info>\n\n**{target_date}**\n\n**Number of LeetCode Questions Solved:** {count}\n\n"
        final_str += "**Questions Solved:**\n"
        for title in question_titles:
            final_str += f"- {title}\n"
        final_str += f"\n\n</blockquote>"
    else:
        final_str = f"<blockquote class=danger>\n\n**{target_date}**\n\n**NO LeetCode Questions Solved**\n\n</blockquote>"

    post_to_webex(app_config.BOT_TOKEN, app_config.ROOM_ID, final_str)
