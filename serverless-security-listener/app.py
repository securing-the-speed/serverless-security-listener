from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route("/webhook")
# generate a function that uploads a payload to s3
def hookshot_to_s3():
    def upload_to_s3(payload):
        # upload payload to s3
        # upload a file to an s3 bucket
        import boto3
        s3 = boto3.client('s3')  
        s3.upload_file(payload, 'mybucket', 'myobject')
        return jsonify(message='Payload uploaded to s3!')

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
