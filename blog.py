from flask import Flask,render_template,request

app =Flask(__name__)

@app.route("/")
def home():
    return render_template("feedbackhome.html")

@app.route("/feedback",methods = ["POST","GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message =request.form.get("message")

        return render_template("thankyou.html", name=name,message=message)

    return render_template("feedback.html")


if __name__=="__main__":
    app.run(debug=True)