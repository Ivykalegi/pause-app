from flask import Flask, render_template


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

app = Flask(__name__)

@app.get("/")
def hello():
    return current_time


if __name__ == "__main__":
    app.run()