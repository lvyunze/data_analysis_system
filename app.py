
from flask import Flask
from flask_cors import CORS
from job_data.cities_in_province import cities_in_province_data
from job_data.employment_area import employment_area_data
from job_data.industrial_distribution import industrial_distriburtion_data
from job_data.professional_distribution import professional_distriburtion_data
from job_data.regional_distribution import regional_distribution_data
from job_data.unit_distribution import unit_distribution_data


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

app.register_blueprint(cities_in_province_data)
app.register_blueprint(employment_area_data)
app.register_blueprint(industrial_distriburtion_data)
app.register_blueprint(professional_distriburtion_data)
app.register_blueprint(regional_distribution_data)
app.register_blueprint(unit_distribution_data)


@app.route('/')
def hello_world():
    return 'nihoa'
    # return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True)
