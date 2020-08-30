from flask import Flask, render_template, request
import subprocess
import os

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = "DefaultSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/docs/")
def docs_index():
    return render_template("docs/introduction.html", docs=get_docs(""))

@app.route("/docs/<doc>")
def docs(doc):
    return render_template(f"docs/{doc}.html", docs=get_docs(doc))

def get_docs(selected):
    docs = [
        ["", "Introduction"],
        ["rep-based-studying", "Rep Based Studying"],
        ["about-us", "About Us"]
    ]
    return [x + [x[0]==selected] for x in docs]

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
