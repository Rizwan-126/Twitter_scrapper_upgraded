from flask import Flask
from flask_mail import Mail
import os
template_dir = os.path.abspath('../templates')

app = Flask(__name__, template_folder=template_dir)
app.debug = True
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'maliksblr92@gmail.com'
app.config['MAIL_PASSWORD'] = 'sfyftjqdwkqmizbm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
