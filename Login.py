from flask import Flask,request,Response,sessions,url_for,redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username= request.form.get("username")
        password= request.form.get("password")

        if username =="admin" and password =="123":
            return redirect(url_for("Welcome"))

        else:
            return Response(
                "Invalid Credentials.Try Again!!",mimetype = "text/plain"
            )

    return '''
         <h2>Login Form</h2>
         <form method = "POST">
         Username:<input type="text" name="Username"><br>
         Password:<input type="text" name="password"><br>
'''    