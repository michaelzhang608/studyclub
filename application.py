from flask import Flask, render_template, request
import os
from flask_socketio import SocketIO
import subprocess

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = "DefaultSecret"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")



# Run Flask if file is interpreted
if __name__ == "__main__":
    os.environ["FLASK_APP"] = "application.py"

    try:
        current = subprocess.check_output(["lsof", "-t", "-i:5000"])
        current = max(current.decode("utf-8").split("\n"))
        print(f"kill {current}")
        os.system(f"kill {current}")
    except:
        pass
    os.system("flask run")
