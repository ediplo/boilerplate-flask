import time
import os

from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'DEBUG': True,
    'SERVER_URL': os.getenv("ELASTIC_APM_SERVER_URL"),
    'SERVICE_NAME': os.getenv("ELASTIC_APM_SERVICE_NAME"),
    'ENVIRONMENT': os.getenv("ELASTIC_APM_ENVIRONMENT"),
    'SECRET_TOKEN': os.getenv("ELASTIC_APM_SECRET_TOKEN"),
}

apm = ElasticAPM(app)

@app.route('/foo')
def darling():
    darling_data: dict = {
        "foo": "bar",
    }
    1/0
    return jsonify(darling_data)
