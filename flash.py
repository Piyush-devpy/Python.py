from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)
app.secret_key = "8888"


@app.route("/")
def home():
    return render_template("flashhome.html")


@app.route("/form", methods=["POST", "GET"])
def form():

    if request.method == "POST":
        name = request.form.get("username")

        if not name:
            flash("Name cannot be empty")
            return render_template("form.html")

        flash(f"Thank you! {name}, your response is submitted!")
        return render_template("thankyou.html")

    # This handles GET request
    return render_template("form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
