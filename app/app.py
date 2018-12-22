from flask import Flask, jsonify, request

from model import Incident, User

app = Flask(__name__)

redflags = []


@app.route('/')
def testing12():
    return 'Flask is working'

@app.route('/api/v1/red-flags', methods=['POST'])
def create_red_fag():
    request_data = request.get_json()

    incident_id = request_data['id']
    createdOn = request_data['createdOn']
    createdBy = request_data['createBy']
    location = request_data['location']
    typeof = request_data['type']
    status = request_data['status']
    images = request_data['Images']
    videos = request_data['Videos']
    comment = request_data['comment']

    new_red_flag = Incident(incident_id, createdOn, createdBy, location, typeof, status, images, videos, comment)

    redflags.append(new_red_flag)

    return jsonify({"status":201, "New Red Flag": new_red_flag.__dict__})


if __name__ == '__main__':
    app.run(debug=True)