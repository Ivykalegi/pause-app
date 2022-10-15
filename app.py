from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def timer():
    return render_template("timer.html")


if __name__ == "__main__":
    app.run(port=5001)
