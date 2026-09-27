from flask import Flask,session,request,Response,render_template

app =Flask(__name__)
app.secret_key="Secret"

@app.route("/")
def render():
    return render_template("Structure.html")

@app.route("/submit", methods = ["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    
    if username == "Piyush27" and password == "2727":
      return render_template("welcome.html",name=username)
    

if __name__== "__main__":
    app.run(debug=True)