from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    return render_template("index.html")

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=5000)