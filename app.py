import flask
import pickle
import pandas as pd


with open(f'model/dt_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        year = flask.request.form['year']
        population = flask.request.form['population']
        suicides_no = flask.request.form['suicides_no']
        country_k_v = flask.request.form['country_k_v']
        gdp_per_capita = flask.request.form['gdp_per_capita']
        min_age = flask.request.form['min age']
        max_age = flask.request.form['max age']
        generation = flask.request.form['generation']
        gdp_year = flask.request.form['gdp_year']
        input_variables = pd.DataFrame([[year, population, suicides_no, country_k_v, gdp_per_capita, min_age, max_age, generation, gdp_year]],
                                       columns=['year', 'population', 'suicides_no', 'country_k_v', 'gdp_per_capita', 'min age', 'max age',  'generation',  'gdp_year'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'Year':year,
                                                     'Population':population, 
                                                     'Suicides_no':suicides_no, 
                                                     'Country_k_v':country_k_v, 
                                                     'Gdp_per_capita':gdp_per_capita, 
                                                     'Min age':min_age, 
                                                     'Max age':max_age, 
                                                     'Generation':generation,  
                                                     'Gdp_year':gdp_year},
                                     result=prediction,
                                     )    




       
