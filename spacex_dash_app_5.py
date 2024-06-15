# Import required libraries
#in terminal
#python3.8 -m pip install pandas dash
#wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
#wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"
#python3.8 spacex_dash_app.py
import pandas as pd
import dash
import matplotlib.pyplot as plt
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Div([
                                    html.Label("Select Sites"), 
                                    dcc.Dropdown(id='site-dropdown', 
                                                 options=[
                                                     {'label':'All Sites', 'value':'ALL'},
                                                     {'label':'CCAFS LC-40', 'value':'CCAFS LC-40'},
                                                     {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},
                                                     {'label':'KSC LC-39A', 'value':'KSC LC-39A'},
                                                     {'label':'CCAFS SLC-40', 'value':'CCAFS SLC-40'}
                                                 ],
                                                 searchable=True,
                                                 value='ALL',
                                                 placeholder = 'Select Launch Site Here',
                                                 )]),
                                html.Br(),
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id = 'payload-slider',
                                                min = 0,
                                                max = 10000,
                                                step = 1000,
                                                marks = {0:'0', 2000: '2000', 4000: '4000', 
                                                         6000: '6000', 8000: '8000', 10000: '10000'},
                                                value = [min_payload, max_payload]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id = 'success-pie-chart', component_property='figure'),
              Input(component_id = 'site-dropdown', component_property='value'))

def update_chart_pie(sites_sel):
    #We want to return all success launches for all sites if 'ALL' is selected
    #In the df, there's class 1 and class 0, 1 = success, 0 = otherwise. So I will filter out each of these separately.
    spacex_1 = spacex_df[spacex_df['class'] == 1] #shape[0] should be 24
    spacex_1_processed = spacex_1.groupby('Launch Site')['class'].sum().reset_index().rename(columns={'class':'success'})

    if sites_sel == 'ALL':
        #Add a pie chart to show the total successful launches count for all sites
        fig = px.pie(spacex_1_processed, values = 'success', names = 'Launch Site',title='Successful Launches from All Sites')
        return fig
    else: 
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        spacex_df_processed = spacex_df.groupby(['Launch Site'])['class'].value_counts().reset_index(name='count')
        fig = px.pie(spacex_df_processed[spacex_df_processed['Launch Site'] == sites_sel], values = 'count', names = 'class')
        fig.update_layout(title='Successful Launches from ' + sites_sel)
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id = 'success-payload-scatter-chart', component_property = 'figure'),
              [Input(component_id = 'site-dropdown', component_property = 'value'),
               Input(component_id = 'payload-slider', component_property = 'value')])

def update_chart_scatter(sites_sel, payload_val):
    payload_low, payload_high = payload_val
    if sites_sel == 'ALL':
        modified_df = spacex_df
        modified_df = modified_df[(modified_df['Payload Mass (kg)'] > payload_low) & (modified_df['Payload Mass (kg)'] < payload_high)]
        fig = px.scatter(modified_df, x='Payload Mass (kg)', y='class', color='Booster Version Category')
        fig.update_layout(title="Payload Mass and the Outcome from All Launch Sites")
        return fig
    else: 
        site_df = spacex_df[spacex_df['Launch Site'] == sites_sel]
        site_df = site_df[(site_df['Payload Mass (kg)'] > payload_low) & (site_df['Payload Mass (kg)'] < payload_high)]
        fig = px.scatter(site_df, x='Payload Mass (kg)', y='class', color='Booster Version Category')
        fig.update_layout(title="Payload Mass Between " + str(payload_low) + "-" + str(payload_high) + " kg " +"and Its Outcome of The Launch at Site " + sites_sel)
        return fig
if __name__ == '__main__':

  app.run_server(port = 8090)
# Run the app
if __name__ == '__main__':
    app.run_server()