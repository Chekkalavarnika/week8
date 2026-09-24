from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def registration():
    return render_template("registration.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    gender = request.form.get("gender")


    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
