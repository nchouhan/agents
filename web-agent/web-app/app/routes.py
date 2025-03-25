from flask import Blueprint, render_template, request
from app.main import main  # Import the main function from main.py

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(user_input)
        # Call the main function with the user input
        result = main(user_input)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)