import boto3
from flask import Flask, jsonify, make_response

app = Flask(__name__)

def upload_to_s3(payload):
    s3 = boto3.client('s3')
    s3.put_object(Bucket='security-listener-bucket', Key='payload)', Body=payload)
    return    


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route("/webhook")
def hookshot_to_s3():
        return jsonify(message='Payload uploaded to s3!')

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
