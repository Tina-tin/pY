# import flask
from flask import Flask, request, render_template

# initialize app
app = Flask(__name__)

# This decorator associates the index function with the URL '/'.
# When you access the '/' Flask will call the index function.
@app.route('/')
def index():
    # This function loads the ship.html template from the templates folder.
    # The ship.html template is then rendered and returned as the response.
    return render_template('ship.html')


# This decorator associates the check function with the URL '/check' and specifies that it should only respond to
# HTTP POST requests.
@app.route('/check', methods=['POST'])
def check():

    #  retrieves the value of the 'passengers' field from the submitted form data.
    passengers = int(request.form['passengers'])

    #  retrieves the value of the 'boats' field from the submitted form data.
    boats = int(request.form['boats'])

    # Each boat can hold 90 people
    total_capacity = boats * 90
    if total_capacity >= passengers:
        result = "There are enough float boats for all passengers."
    else:
        result = "There are not enough float boats for all passengers."

    return render_template('ship.html', result=result)

if __name__ == '__main__':
    # This method runs the Flask application.
    app.run(debug=True)
