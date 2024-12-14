import os
from backend import create_app
from flask import render_template

# Create Flask app instance
app = create_app()

@app.route('/')
def home():
    return render_template('index.html')  # This serves the `index.html` file

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5500))  # Default to 5500 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
