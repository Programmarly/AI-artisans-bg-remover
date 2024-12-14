from backend import create_app
from flask import render_template
from dotenv import load_dotenv
import os

load_dotenv()
PORT = os.getenv("PORT") or 5500 

# Create Flask app instance
app = create_app()
@app.route('/')
def home():
    return render_template('index.html')  # This serves the `index.html` file

if __name__ == '__main__':
    app.run(port= PORT,debug=True)
