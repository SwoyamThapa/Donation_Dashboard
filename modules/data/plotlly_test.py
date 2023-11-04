import json
import plotly.express as px
import pandas as pd

# Load the JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Create a bar chart with 'goal' and 'funding' bars side by side
fig = px.bar(df, x='title', y=['goal', 'funding'], title='Project Funding vs. Goal',
             labels={'title': 'Project Title', 'value': 'Amount'},
             barmode='group')  # Set barmode to 'group'

# Show the chart
fig.show()
