import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np

df_raw = pd.read_csv('https://bit.ly/elements-periodic-table')
df_raw.to_csv("raw.csv")

def identity(x): return x

app = dash.Dash(__name__)

app.layout = html.Div(
    className="main",
    children=[
        html.H2("Periodic Table"),
        html.P("Choose the value to display"),
        dcc.Dropdown(id = 'valagg',
                     options=[{'label': 'Symbol', 'value': 'Symbol, identity'},
                              {'label': 'Element', 'value': 'Element, identity'},
                              {'label': 'Atomic Number, mean', 'value': 'AtomicNumber, mean'},
                              {'label': 'Atomic Number, max', 'value': 'AtomicNumber, max'},
                              {'label': 'Atomic Number, min', 'value': 'AtomicNumber, min'},
                              {'label': 'Atomic Mass, mean', 'value': 'AtomicMass, mean'},
                              {'label': 'Atomic Mass, max', 'value': 'AtomicMass, max'},
                              {'label': 'Atomic Mass, min', 'value': 'AtomicMass, min'},
                              {'label': 'Number Of Neutrons, mean', 'value': 'NumberOfNeutrons, mean'},
                              {'label': 'Number Of Neutrons, max', 'value': 'NumberOfNeutrons, max'},
                              {'label': 'Number Of Neutrons, min', 'value': 'NumberOfNeutrons, min'},
                              {'label': 'Electronegativity, mean', 'value': 'Electronegativity, mean'},
                              {'label': 'Electronegativity, max', 'value': 'Electronegativity, max'},
                              {'label': 'Electronegativity, min', 'value': 'Electronegativity, min'},
                              {'label': 'First Ionization Energy, mean', 'value': 'FirstIonization, mean'},
                              {'label': 'First Ionization Energy, max', 'value': 'FirstIonization, max'},
                              {'label': 'First Ionization Energy, min', 'value': 'FirstIonization, min'},
                              {'label': 'Density, mean', 'value': 'Density, mean'},
                              {'label': 'Density, max', 'value': 'Density, max'},
                              {'label': 'Density, min', 'value': 'Density, min'},
                              {'label': 'Year, mean', 'value': 'Year, mean'},
                              {'label': 'Year, max', 'value': 'Year, max'},
                              {'label': 'Year, min', 'value': 'Year, min'},
                             ],
                        value='Symbol, identity'),
        html.P("Choose the row and column"),
        dcc.Dropdown(id = 'rowcol',
                     options=[{'label': 'Period, Group', 'value': 'Period, Group'},
                               {'label': 'Period, Phase', 'value': 'Period, Phase'},
                               {'label': 'Period, Type', 'value': 'Period, Type'},
                               {'label': 'Period, NumberOfShells', 'value': 'Period, NumberOfShells'},
                               {'label': 'Period, NumberOfValence', 'value': 'Period, NumberOfValence'},
                               {'label': 'Group, Phase', 'value': 'Group, Phase'},
                               {'label': 'Group, Type', 'value': 'Group, Type'},
                               {'label': 'Group, NumberOfShells', 'value': 'Group, NumberOfShells'},
                               {'label': 'Group, NumberOfValence', 'value': 'Group, NumberOfValence'},
                               {'label': 'Phase, Type', 'value': 'Phase, Type'},
                               {'label': 'Phase, NumberOfShells', 'value': 'Phase, NumberOfShells'},
                               {'label': 'Phase, NumberOfValence', 'value': 'Phase, NumberOfValence'},
                               {'label': 'Type, NumberOfShells', 'value': 'Type, NumberOfShells'},
                               {'label': 'Type, NumberOfValence', 'value': 'Type, NumberOfValence'},
                               ],
                        value='Period, Group'),
        html.P("Click the button to refresh"),
        html.Button("Refresh!", id="go"),
        html.P("Here is the table:"),
        html.Div(id = 'table')
    ]
)

@app.callback(
    Output(component_id='table', component_property='children'),
    Input(component_id='go', component_property='n_clicks'),
    State(component_id='rowcol', component_property='value'),
    State(component_id='valagg', component_property='value'),
)
def get_table(n_clicks, 
              rowcol, valagg):
    
    agg_fun_dict = {"identity":identity, 
                    "min":min, 
                    "max":max, 
                    "mean":np.mean}
    
    row_col_dict = {'Period, Group': ('Period', 'Group'),
                    'Period, Phase': ('Period', 'Phase'),
                    'Period, Type': ('Period', 'Type'),
                    'Period, NumberOfShells': ('Period', 'NumberOfShells'),
                    'Period, NumberOfValence': ('Period', 'NumberOfValence'),
                    'Group, Phase': ('Group', 'Phase'),
                    'Group, Type': ('Group', 'Type'),
                    'Group, NumberOfShells': ('Group', 'NumberOfShells'),
                    'Group, NumberOfValence': ('Group', 'NumberOfValence'),
                    'Phase, Type': ('Phase', 'Type'),
                    'Phase, NumberOfShells': ('Phase', 'NumberOfShells'),
                    'Phase, NumberOfValence': ('Phase', 'NumberOfValence'),
                    'Type, NumberOfShells': ('Type', 'NumberOfShells'),
                    'Type, NumberOfValence': ('Type', 'NumberOfValence')}
    
    val_agg_dict = {'Symbol, identity': ('Symbol', 'identity'),
                    'Element, identity': ('Element', 'identity'),
                    'AtomicNumber, mean': ('AtomicNumber', 'mean'),
                    'AtomicNumber, max': ('AtomicNumber', 'max'),
                    'AtomicNumber, min': ('AtomicNumber', 'min'),
                    'AtomicMass, mean': ('AtomicMass', 'mean'),
                    'AtomicMass, max': ('AtomicMass', 'max'),
                    'AtomicMass, min': ('AtomicMass', 'min'),
                    'NumberOfNeutrons, mean': ('NumberOfNeutrons', 'mean'),
                    'NumberOfNeutrons, max': ('NumberOfNeutrons', 'max'),
                    'NumberOfNeutrons, min': ('NumberOfNeutrons', 'min'),
                    'Electronegativity, mean': ('Electronegativity', 'mean'),
                    'Electronegativity, max': ('Electronegativity', 'max'),
                    'Electronegativity, min': ('Electronegativity', 'min'),
                    'FirstIonization, mean': ('FirstIonization', 'mean'),
                    'FirstIonization, max': ('FirstIonization', 'max'),
                    'FirstIonization, min': ('FirstIonization', 'min'),
                    'Density, mean': ('Density', 'mean'),
                    'Density, max': ('Density', 'max'),
                    'Density, min': ('Density', 'min'),
                    'Year, mean': ('Year', 'mean'),
                    'Year, max': ('Year', 'max'),
                    'Year, min': ('Year', 'min')}

    if rowcol not in row_col_dict:
        rowcol = "Period, Group"
        
    if valagg not in val_agg_dict:
        valagg = "Symbol, identity"

    df = pd.read_csv('raw.csv')
    
    
    row, col = row_col_dict[rowcol]
    val, agg = val_agg_dict[valagg]
    
    agg_function = agg_fun_dict[agg]
    

    df_return = df.pivot_table(index = row,
                               columns = col, 
                               values = val,
                               aggfunc = agg_function, 
                               fill_value = ".")

    if val in ["Symbol", "Element"]:
        df_return = df_return.applymap(lambda x: str(x).replace("[]", ".."))

    df_return = df_return.reset_index(drop = False)
    df_return = df_return.rename(
                    columns={df_return.columns[0]: row + r' \ ' + col}
                    )


    
    table_in_dash = [dash_table.DataTable(
                        id = 'table-update',
                        columns = [{"name": str(i), "id": str(i)} 
                                 for i 
                                 in df_return.columns],
                        data = df_return.to_dict('records'), 
                        style_data = {'whiteSpace': 'nowrap'},
                        
                        ) 
                    ]


    return table_in_dash



app.run_server(debug=True, host="0.0.0.0")