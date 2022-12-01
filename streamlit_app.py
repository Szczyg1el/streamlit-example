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
from pathlib import Path 
github_issues= json.loads(Path("ss.json").read_text())
github_issue = github_issues[0]

st.write(github_issue) 