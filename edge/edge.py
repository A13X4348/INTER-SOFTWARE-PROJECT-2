import requests
from flask import Flask, Response

app = Flask(__name__)

ORIGIN_SERVER_URL = "http://origin:5000"
cache = {}

@app.route("/audio/<filename>")
def get_audio(filename):
    if filename in cache:
        print (f"Cache HIT for {filename}")
        return Response(cache[filename], content_type='audio/mpeg')
    
    print(f"Cache MISS for {filename}")
    origin_url = f"{ORIGIN_SERVER_URL}/audio/{filename}"

    try:
        response = requests.get(origin_url)

        if response.status_code == 200:
            print(f"Storing {filename} in cache")
            cache[filename] = response.content
            return Response(response.content, content_type='audio/mpeg')
        else:
            return "File not found on origin server", response.status_code

    except requests.exceptions.RequestException as e:
        return f"Error connecting to origin server: {e}", 502
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)