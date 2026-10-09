
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "1111"


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")


@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        flash(f"Welcome, {name}! You are registered.")
        return redirect(url_for("success"))

    return render_template("register.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
