from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html', title = 'index')

@app.route('/topSoftwares')
def top_softwares():
    return render_template('topSoftware.html')

@app.route('/osVulnerabilities')
def osVulnerabilities():
    return render_template('osVulnerabilities.html')

@app.route('/mostCVE')
def mostCVE():
    return render_template('mostCVE.html')

@app.route('/vulnerablePC')
def vulnerablePC():
    return render_template('vulnerablePC.html')

@app.route('/layout')
def layout():
    return render_template('layout.html', title = 'layout')