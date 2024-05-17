from application import app
from flask import render_template

# Route for the index page
@app.route("/")
def index():
    # Renders the index.html template with the title "Dashboard"
    return render_template('index.html', title='Dashboard')

# Route for the topSoftwares page
@app.route('/topSoftwares')
def top_softwares():
    # Renders the topSoftware.html template
    return render_template('topSoftware.html')

# Route for the osVulnerabilities page
@app.route('/osVulnerabilities')
def osVulnerabilities():
    # Renders the osVulnerabilities.html template
    return render_template('osVulnerabilities.html')

# Route for the mostCVE page
@app.route('/mostCVE')
def mostCVE():
    # Renders the mostCVE.html template
    return render_template('mostCVE.html')

# Route for the vulnerablePC page
@app.route('/vulnerablePC')
def vulnerablePC():
    # Renders the vulnerablePC.html template
    return render_template('vulnerablePC.html')

# Route for the yearLine page
@app.route('/yearLine')
def yearLine():
    # Renders the yearLine.html template
    return render_template('yearLine.html')

# Route for the severityPie page
@app.route('/severityPie')
def severityPie():
    # Renders the severityPie.html template
    return render_template('severityPie.html')

# Route for the layout page
@app.route('/layout')
def layout():
    # Renders the layout.html template with the title "layout"
    return render_template('layout.html', title='layout')
