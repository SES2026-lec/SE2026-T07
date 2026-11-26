from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/member-c0c25036")
def member_c0c25036():
    return "T07 member: C0C25036"

@app.route("/member-c0c26031")
def member_c0c26031():
    return "T07 member: C0C26031"

@app.route("/member-C0C25085")
def member_c0c25085():
    return "T07 member:C0C25085 "
