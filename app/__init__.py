from flask import Flask 
from flask_mail import Mail
import os  

def create_app():
    app = Flask(__name__)
    
    app.config['MAIL_SERVER']= 'smtp.office365.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'donshirokuma@gmail.com'
    app.config['MAIL_PASSWORD'] = 'estigia9696'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    # app.config['MAIL_DEFAULT_SENDER'] = "donshirokuma@outlook.com"

    mail = Mail(app) 
    from . import portfolio 

    app.register_blueprint(portfolio.bp) 
    return app 

