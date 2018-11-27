import dash, dash_core_components, dash_html_components
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children='Dash Tutorials')

if __name__ == '__main__':
    app.run_server(debug=True)