import requests

from settings import app_config


def fetch_recent_submissions(username, limit=30) -> dict:
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
