from flask import Flask,session,request,Response,render_template

app =Flask(__name__)
app.secret_key="Secret"

@app.route("/")
def render():
    return render_template("Structure.html")