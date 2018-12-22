import unittest
import requests
from model import Incident, User
import flask
import json
import datetime
from app import app

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_post_status(self): 

        flag_data = {
            'id':1234,
            'createdOn':datetime.datetime.today().strftime('%Y-%m-%d'), 
            'createBy': 4747583,
            'type': 'intervention',
            'status':'status',
            "location": 'ntinda',
            'Images':['kiaosoa.jpg'],
            'Videos':['najska.jpg'],
            'comment':'Self test comment',
            } 

        response = requests.post('http://127.0.0.1:5000/api/v1/red-flags', json=flag_data)
        status = 201
        self.assertEqual(response.status_code, status)


    def test_incident_input(self):
        pass




        


