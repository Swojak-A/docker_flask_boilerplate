from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

	html = "<h3>M'Lady!</h3>"

	return html

if __name__ == "__main__":
    app.run()