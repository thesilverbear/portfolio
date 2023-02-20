from flask import (
    Blueprint, Flask, url_for, redirect, render_template, request, current_app 
)
from flask_mail import Mail, Message
import smtplib

bp = Blueprint('portfolio', __name__, url_prefix='/') 
app = Flask(__name__) 

app.config['MAIL_SERVER']= 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'donshirokuma@outlook.com'
app.config['MAIL_PASSWORD'] = 'estigia9696'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEFAULT_SENDER'] = "donshirokuma@outlook.com"

mail = Mail(app) 


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html') 





@bp.route('/mail', methods=['POST', 'GET'])
def mailing():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        mi_email = 'donshirokuma@outlook.com'

        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-mail: {email}\n \n{message}", sender='donshirokuma@outlook.com', recipients=['donshirokuma@outlook.com'])
        mail.send(msg) 

        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index')) 




