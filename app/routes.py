from flask import render_template
from app import app
from app.forms import LeadForm, NewsletterForm

@app.route('/')
@app.route('/index')
def index(): 
    form = LeadForm()
    form2 = NewsletterForm()
    return render_template('index.html', form=form, form2 = form2)
    