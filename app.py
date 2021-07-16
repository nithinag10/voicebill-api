import flask as Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome Home machas"


if __name__ == "__main__":
    app.run()