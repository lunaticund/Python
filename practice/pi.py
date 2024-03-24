import plotly.graph_objs as go

# 二维线图
trace = go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines')
data = [trace]
layout = go.Layout(title='2D Line Plot')
fig = go.Figure(data=data, layout=layout)
fig.show()
