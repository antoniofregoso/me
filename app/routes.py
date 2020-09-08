import os
from flask import render_template,  send_from_directory, request, redirect 
from app import app
from app.forms import LeadForm, NewsletterForm

@app.route('/')
@app.route('/index')
def index(): 
    qs = request.args
    form = LeadForm()
    form2 = NewsletterForm()
    return render_template('index.html', form=form, form2 = form2)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    