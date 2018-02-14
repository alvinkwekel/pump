# Getting Started
sudo apt-get update
sudo apt-get install python3-pip
pip3 install virtualenv
virtualenv venv
. venv/bin/activate
pip install flask
FLASK_APP=pump.py flask run

# Documentation
http://flask.pocoo.org/snippets/119/
http://flask.pocoo.org/docs/0.12/api/#flask.json.jsonify
