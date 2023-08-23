from flask import Blueprint

views = Blueprint('views', __name__name)



@views.route('/')
def home():

 return "<h1>Test</h1>"
