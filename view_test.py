import json
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Specify the file path to your locally saved JSON file
file_path = 'modules/data/data.json'

# Load the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Create a dictionary with organization names as keys and lists of countries as values
org_country_dict = {}

for entry in data:
    org = entry.get('organization')
    org_name = org.get('name')
    countries = org.get('countries').get('country')

    for country in countries:
        if org_name in org_country_dict:
            org_country_dict[org_name].append(country.get('name'))
        else:
            org_country_dict[org_name] = [country.get('name')]

# Convert the dictionary into a DataFrame
df = pd.DataFrame.from_dict(org_country_dict, orient='index').T.melt(value_name='Country', var_name='Organization')
df = df.dropna(subset=['Country'])

# Create a map with different colors for each organization
fig1 = go.Figure()

unique_organizations = df['Organization'].unique()
color_mapping = {}  # To store color mapping for organizations

for idx, organization in enumerate(unique_organizations):
    color = px.colors.qualitative.Plotly[idx % len(px.colors.qualitative.Plotly)]
    color_mapping[organization] = color
    subset_df = df[df['Organization'] == organization]
    text = subset_df['Organization'] + '<br>' + subset_df['Country']

    fig1.add_trace(go.Scattergeo(
        locationmode="country names",
        locations=subset_df['Country'],
        text=text,
        marker=dict(size=10, color=color),
        name=organization,  # Set the trace name to the organization name
    ))

fig1.update_layout(
    title="Organization's operation country",
    geo=dict(showland=True, landcolor="lightgray"),
    legend_title_text='Organizations',  # Customize the legend title
)

# Create a bar chart with 'goal' and 'funding' bars side by side
fig2 = px.bar(df, x='title', y=['goal', 'funding'], title='Project Funding vs. Goal',
             labels={'title': 'Organization', 'value': 'Amount'},
             barmode='group')  # Set barmode to 'group'

projects = []

for entry in data:
    org = entry.get('organization')

    projects_info = {
        'organization': org.get('name'),
        'totalProjects': org.get('totalProjects'),
        'activeProjects': org.get('activeProjects')
    }

    if not projects_info in projects:
        projects.append(projects_info)

df = pd.DataFrame(projects)

# Create a bar chart with 'goal' and 'funding' bars side by side
fig3 = px.bar(df, x='organization', y=['totalProjects', 'activeProjects'], title='TotalProjects and ActiveProjects',
              labels={'title': 'Organization', 'value': 'No. of Projects'},
              barmode='group')  # Set barmode to 'group'

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(dcc.Graph(figure=fig1), style={'width': '33%', 'display': 'inline-block'}),
    html.Div(dcc.Graph(figure=fig2), style={'width': '33%', 'display': 'inline-block'}),
    html.Div(dcc.Graph(figure=fig3), style={'width': '33%', 'display': 'inline-block'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
