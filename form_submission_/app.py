from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  

# MongoDB Atlas connection
client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = client['formDB']
collection = db['submissions']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            # Insert data into MongoDB
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))

        except Exception as e:
            flash(f"Error: {str(e)}")  # Display error on same page

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
