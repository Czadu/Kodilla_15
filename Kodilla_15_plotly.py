import plotly.graph_objects as go

salaries = [
    ("Mark", 1000),
    ("John", 1500),
    ("Daniel", 2300),
    ("Greg", 5000)
]

names, salary = zip(*salaries)

fig = go.Figure(data=[
    go.Bar(
        y=salary,   
        x=names, 
        orientation='v',
        marker_color='green'

    )
])

fig.update_layout(
    title='Salaries',
    xaxis_title='Salary',
    yaxis_title='Name'
)

fig.show()
