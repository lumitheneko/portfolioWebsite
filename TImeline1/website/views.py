from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@views.route('/My-python-code')
def python():
    return render_template("pythonJournal.html")


@views.route('/My-HTML-code')
def HTML():
    return render_template("webdevJournal.html")
