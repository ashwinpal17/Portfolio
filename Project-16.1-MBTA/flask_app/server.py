from threading import Timer
from flask import Flask, render_template, jsonify
import time, json
from MBTAApiClient import callMBTAApi

app = Flask(__name__)
buses = []

def refresh():
    global buses
    try:
        buses = callMBTAApi()
    except Exception as e:
        print(f"[{time.ctime()}] refresh failed:", e)
    Timer(10, refresh).start()

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/location")
def location():
    return jsonify(buses)

if __name__ == "__main__":
    print("[BOOT] starting background refresher…")
    refresh()
    print("[BOOT] starting Flask on http://127.0.0.1:3000 …")
    app.run(port=3000, debug=True)
