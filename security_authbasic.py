#curl -u john:hello http://127.0.0.1:7002/
import os
from ipaddress import ip_address
from flask import Flask, redirect, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "login.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app = Flask(__name__)
dblogin = SQLAlchemy(app)
auth = HTTPBasicAuth()
# nama kelompok 
# Arief Rachman (6A - 19090012) 
# M. Rizqi Fauzi Maksum (6A = 19090132) 
class login(dblogin.Model):
    username = dblogin.Column(dblogin.String(80), unique=True, nullable=False, primary_key=True)
    password = dblogin.Column(dblogin.String(100))
    keterangan = dblogin.Column(dblogin.String(100))
    def toJson(self):
        return {"username": self.username}

    def __repr__(self):
        return json.dumps(self.__dict__)
users = login.query.all()
pswd=generate_password_hash("123")
print(pswd)
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    ##redirect("localhost:4000/api/v2/users/info")

@app.route('/api/v1/login') 
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug = True, port=4000)
