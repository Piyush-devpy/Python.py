from flask import Flask,request,Response,render_template

app= Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="Piyush",
        is_topper=True,
        subjects = [
            'Science',
            'Maths',
            'Biology'
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)