from flask import Flask, render_template, request, redirect
import subprocess
import os

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = "DefaultSecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("docs/404.html", docs=get_docs())

@app.route("/docs/")
def docs_index():
    return render_template("docs/introduction.html", docs=get_docs(""))

@app.route("/docs/<doc>")
def docs(doc):
    try:
        return render_template(f"docs/{doc}.html", docs=get_docs(selected=doc))
    except:
        return redirect('/docs/')

def get_docs(selected=None):
    docs = [
        ["h", "OVERVIEW", ""],
        ["d", "Introduction", ""],
        ["d", "Rep Based Studying", "rep-based-studying"],
        ["d", "About Us", "about-us"],
    ]
    if selected:
        for d in docs:
            if d[0] == "d" and d[2] == selected:
                d[0] = "s"
                break
    return docs

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
