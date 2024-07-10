from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(_name_)

# Sample data storage (you can use a database or file storage as per your project needs)
data_store = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    new_data = request.form['new_data']
    data_store.append(float(new_data))  # Convert to appropriate data type if needed
    return redirect('/')

@app.route('/calculate_probability')
def calculate_probability():
    # Example calculation (replace with your own logic)
    if data_store:
        total = sum(data_store)
        probability = total / len(data_store)
        return f'Probability: {probability}'
    else:
        return 'No data available.'

if _name_ == '_main_':
    app.run(debug=True)