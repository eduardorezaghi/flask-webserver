from flask import Flask
from flask import render_template
from flask import request, make_response, jsonify


# >> $env:FLASK_ENV = "development"
# >> $env:FLASK_APP = "app"
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
