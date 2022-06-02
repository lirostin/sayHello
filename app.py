from flask import Flask, render_template, request, flash
from db import get_counter

app = Flask(__name__)
app.secret_key = "mysecretkey"
temp = get_counter()
print(temp)
@app.route("/hello")
def index():
    flash(f"""Today is {".".join(str(temp)[-13:-3].split(", "))} 
    Tell us, what's your name? 
    """)
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)