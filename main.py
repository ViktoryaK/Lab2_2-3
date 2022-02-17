"""
This is the main module of the web app
"""
from flask import Flask, request
from flask import render_template
from web_application import get_names_locations
from twitter2 import create_json
from web_application import map_creation

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index_html():
    return render_template('index.html')


@app.route('/send_data', methods=['POST'])
def get_data_from_html():
    """
    This function is asking a user for input
    """
    user = request.form['user']
    print("Twitter user name is " + user)
    map_creation(get_names_locations(create_json(user)))
    return render_template('index.html')


@app.route('/send_data/Friends', methods=['POST'])
def finally_map():
    ip = request.remote_addr
    return render_template('Friends.html', user_ip=ip)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
