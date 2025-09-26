from flask import Flask, send_from_directory, jsonify
import os
import requests

EDGE_SERVERS = [
    "http://edge1:5001",  # hostname:port for edge 1
    "http://edge2:5002",  # hostname:port for edge 2
]

app = Flask(__name__)

# Path to audio files
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio_files")

@app.route("/")
def home():
    return jsonify({"message": "Origin server is running"}), 200

# Serve audio files
@app.route("/audio/<filename>")
def get_audio(filename):
    
    try:
        return send_from_directory(AUDIO_DIR, filename)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

# Notify edges about updates
@app.route("/update/<filename>", methods=["POST"])
def update_file(filename):
    responses = []
    for edge in EDGE_SERVERS:
        try:
            url = f"{edge}/invalidate/{filename}"
            r = requests.post(url)
            responses.append({edge: r.json()})
        except Exception as e:
            responses.append({edge: str(e)})

    return jsonify({
        "message": f"Update triggered for {filename}",
        "edge_responses": responses
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
