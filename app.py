tkfrom flask import Flask
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

@app.route("/member-C0C24043")
def member_c0c24043():
    return "T07 member:C0C24043 "

@app.route("/vscode-c0c25036")
def vscode_c0c25036():
    return "T07 vscode: C0C25036"

@app.route("/vscode-c0c26031")
def vscode_c0c26031():
    return "T07 vscode: C0C26031"