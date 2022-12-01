from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

lista = [1,2,3,4,5]
for elem in lista:
    st.write (elem)

slownik = {"imie":"krzysztof", "nazwisko":"kajak"}
st.write (slownik)
# imie=krzystof
# nazwisko=kajak
for key in slownik:
    st.write (key, slownik[key])

for tupl in slownik.items():
    key, value = tupl
    st.write (key, value)

for key, value in slownik.items():
    st.write (key, value)

st.write ("imie", slownik["imie"])


import json
github_issue = json.loads("""
 {
    "url": "https://api.github.com/repos/apache/airflow/issues/28041",
    "repository_url": "https://api.github.com/repos/apache/airflow",
    "labels_url": "https://api.github.com/repos/apache/airflow/issues/28041/labels{/name}",
    "comments_url": "https://api.github.com/repos/apache/airflow/issues/28041/comments",
    "events_url": "https://api.github.com/repos/apache/airflow/issues/28041/events",
    "html_url": "https://github.com/apache/airflow/pull/28041",
    "id": 1471812843,
    "node_id": "PR_kwDOAgUK285EFhwb",
    "number": 28041,
    "title": "Enhance chart to allow over-riding command-line args to statsd exporter",
    "user": {
      "login": "rob-1126",
      "id": 89029510,
      "node_id": "MDQ6VXNlcjg5MDI5NTEw",
      "avatar_url": "https://avatars.githubusercontent.com/u/89029510?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/rob-1126",
      "html_url": "https://github.com/rob-1126",
      "followers_url": "https://api.github.com/users/rob-1126/followers",
      "following_url": "https://api.github.com/users/rob-1126/following{/other_user}",
      "gists_url": "https://api.github.com/users/rob-1126/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/rob-1126/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/rob-1126/subscriptions",
      "organizations_url": "https://api.github.com/users/rob-1126/orgs",
      "repos_url": "https://api.github.com/users/rob-1126/repos",
      "events_url": "https://api.github.com/users/rob-1126/events{/privacy}",
      "received_events_url": "https://api.github.com/users/rob-1126/received_events",
      "type": "User",
      "site_admin": false
    },
    "labels": [
      {
        "id": 1971984525,
        "node_id": "MDU6TGFiZWwxOTcxOTg0NTI1",
        "url": "https://api.github.com/repos/apache/airflow/labels/area:helm-chart",
        "name": "area:helm-chart",
        "color": "024e91",
        "default": false,
        "description": "Airflow Helm Chart"
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [

    ],
    "milestone": null,
    "comments": 1,
    "created_at": "2022-12-01T19:14:49Z",
    "updated_at": "2022-12-01T19:16:55Z",
    "closed_at": null,
    "author_association": "NONE",
    "active_lock_reason": null,
    "draft": false,
    "pull_request": {
      "url": "https://api.github.com/repos/apache/airflow/pulls/28041",
      "html_url": "https://github.com/apache/airflow/pull/28041",
      "diff_url": "https://github.com/apache/airflow/pull/28041.diff",
      "patch_url": "https://github.com/apache/airflow/pull/28041.patch",
      "merged_at": null
    },
    "body": "Add a new configurable option (statsd.args) to the helm chart to allow args on the statsd-exporter container to be over-ridden in the same manner as the args on other containers.\r\n",
    "reactions": {
      "url": "https://api.github.com/repos/apache/airflow/issues/28041/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/apache/airflow/issues/28041/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  }
""")
st.write (github_issue) 