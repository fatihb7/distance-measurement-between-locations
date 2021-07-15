# Loading libraries.
from flask import Flask
from calculatedistance import app_calcdist

app = Flask(__name__)
app.register_blueprint(app_calcdist)

# Constant variables.
PORT = 105
ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    app.run(host=ADDRESS, port=PORT)
