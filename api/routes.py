from flask import Flask, jsonify, request

from api.model import Incident, User

app = Flask(__name__)

redflags = []


@app.route('/')
def testing12():
    return 'Flask is working'

@app.route('/api/v1/red-flags', methods=['POST'])
def create_red_flag():

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

    
    # if request.status_code != 201:
    #     return jsonify({'status':'404', 'Error': 'Url not found Or Incorrect'}), 400

    redflags.append(new_red_flag.__dict__)

    print(redflags)

    return jsonify({"status":201, "data": new_red_flag.__dict__}), 201
    
@app.route('/api/v1/red-flags', methods=['GET'])
def get_all_flags():

    if len(redflags) == 0:
        return jsonify({'status':'404', 'Data': 'No record available'}), 404
    
    return jsonify({'redflags': redflags}) 

# @app.route('/api/v1/red-flags/<string:location>', methods=['GET'])
# def get_flag_location(location):
#     for value in redflags:
#         if redflags['location'] == location:
            


if __name__ == '__main__':
    app.run(debug=True)