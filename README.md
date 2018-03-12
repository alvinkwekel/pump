# Getting Started
`sudo apt-get update`

```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```
https://docs.python.org/3/tutorial/venv.html

```
sudo apt install virtualenvwrapper
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3 pump-venv
workon pump-venv
```
https://virtualenvwrapper.readthedocs.io/en/latest/

```
pip install flask flask-cors
FLASK_APP=pump.py flask run
deactivate
```
https://flask-cors.readthedocs.io/en/latest/

# Documentation
* http://flask.pocoo.org/snippets/119/
* http://flask.pocoo.org/docs/0.12/api/#flask.json.jsonify
