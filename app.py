from flask import Flask
from flask import json
import logging

logging.basicConfig(
    filename='app.log', level=logging.DEBUG, format='%(asctime)s, %(message)s'
)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def serverStatus():
    app.logger.debug("/status endpoint was reached")
    return app.response_class(
        response=json.dumps({"result": "OK - Healthy"}),
        status=200,
        mimetype="application/json"
    )


@app.route("/metrics")
def serverMetrics():
    app.logger.debug("/metrics endpoint was reached")
    return app.response_class(
        response=json.dumps({"status": "success", "code":0, "data": {"UserCount": 190, "ActiveUsers": 30}}),
        status=200,
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
