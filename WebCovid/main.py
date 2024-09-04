'''import requests
url = 'https://api.jikan.moe/v4/top/anime'
datos = requests.get(url)
if datos.status_code == 200:
    datos = datos.json()
    for e in datos['data']:
        print (e['title'])'''

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

COVID_API_URL = "https://api.covidtracking.com/v1/states/current.json"

def fetch_covid_data():
    response = requests.get(COVID_API_URL)
    response.raise_for_status()
    return response.json()

@app.route('/')
def index():
    data = fetch_covid_data()
    states = {state['state']: state for state in data}
    return render_template('index.html', states=states)

@app.route('/state/<state>')
def state_info(state):
    data = fetch_covid_data()
    state_data = next((item for item in data if item['state'] == state.upper()), None)
    return render_template('state_info.html', state_data=state_data)

if __name__ == '__main__':
    app.run(debug=True)

