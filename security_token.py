# curl -H "Authorization: Bearer secret-token-1" http://127.0.0.1:7001/

from flask import Flask
from flask_httpauth import HTTPTokenAuth


app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# nama kelompok 
# Arief Rachman (6A - 19090012) 
# M. Rizqi Fauzi Maksum (6A = 19090142) 
tokens = {
    "secret-token-1": "19090012",
    "secret-token-2": "19090142"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@app.route('/api/v2/users/info')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug = True, port=4000)
