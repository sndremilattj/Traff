from flask import Flask, request, Response, send_from_directory

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return send_from_directory(app.root_path, "index.html")

@app.route("/data_gateway.php", methods=["GET", "POST", "OPTIONS"])
def gateway():
    print("\n=== TRAFF REQUEST ===")
    print("Method:", request.method)
    print("Form:", dict(request.form))
    print("Raw:", request.get_data(as_text=True))
    return Response("OK", mimetype="text/plain")

app.run(host="127.0.0.1", port=5000)