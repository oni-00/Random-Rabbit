from flask import Blueprint, render_template
from flask_login import login_required, current_user
import random, time
import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/rabbit')
@login_required
def rabbit():
    nrandom = random.randint(1,500)
    dt = datetime.datetime.utcnow()
    dtstr = "{}-{}-{} {}:{}:{}".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    return render_template('rabbit.html', value=nrandom, datetime=dtstr)
    