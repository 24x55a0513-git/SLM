from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>

    <body style="text-align:center; background:pink;">

    <h1>Hello My Love ❤️</h1>

    <img src="/static/photo.jpeg" width="300">

    <p>You are my happiness 💖</p>

    </body>

    </html>
    """
if__name__=="__main__":
app.run(debug=True)