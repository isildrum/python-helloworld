from flask import Flask, Response, json
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', 
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s  : %(message)s")

@app.route("/")
def hello():
    app.logger.info('Hello endpoint was reached')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status endpoint was reached')
    return Response(json.dumps({"result": "OK healthy"}), status = 200, mimetype='application/json')

@app.route("/metrics")
def metrics():
    app.logger.info('Metrics endpoint was reached')
    return Response(json.dumps({"status":"success","code":0, "data":{"UserCount":140,"UserCountActive":23}}), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
