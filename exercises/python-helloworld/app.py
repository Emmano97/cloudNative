from flask import Flask, json
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("main request successfully")
    return "Hello World!"


@app.route("/status")
def status():
    response = app.response_class(
        response= json.dumps({
            "result": "OK - healthy"
        }),
        status=200,
        mimetype= "application/json"
    )
    app.logger.info("status request successfully")
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response= json.dumps(
            {
                "status":"success",
                "code":0,
                "data":{
                    "UserCount":140,
                    "UserCountActive":23
                }
            }
        ),
        status=200,
        mimetype= "application/json"
    )
    app.logger.info("metrics request successfully")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
