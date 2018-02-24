import tempfile

from flask import Flask, request, jsonify
import imageio

from engine import NNSearch


app = Flask(__name__)
search_engine = NNSearch("image_files.bin", "index.ann")


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/uploadsearch", methods=["POST"])
def upload_search():
    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(request.files["image"].read())
        image = imageio.imread(tmp.name)

    return jsonify(status="OK")


if __name__ == "__main__":
    app.run(debug=True)
