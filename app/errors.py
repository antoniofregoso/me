from flask import render_template
from app import app
from config import Config 

@app.errorhandler(404)
def not_found_error(error):
    tracking = {'ga':Config.OPTIONS['google'], 'fb':Config.OPTIONS['facebook'], 'at':Config.OPTIONS['addthis']}
    return render_template('404.html', tracking=tracking), 404

@app.errorhandler(500)
def internal_error(error):
    tracking = {'ga':Config.OPTIONS['google'], 'fb':Config.OPTIONS['facebook'], 'at':Config.OPTIONS['addthis']}
    return render_template('500.html', tracking=tracking), 500