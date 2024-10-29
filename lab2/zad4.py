import numpy as np
import plotly.graph_objects as go


x = np.random.normal(loc=0, scale=1, size=1000)
y = np.random.normal(loc=0, scale=1, size=1000)
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
fig.show()
