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
            'id':12435,
            'createdOn':datetime.datetime.today().strftime('%Y-%m-%d'), 
            'createBy': 4747583,
            'type': 'intervention',
            'location': 'ntinda',
            'Images':['kiaosoa.jpg'],
            'Videos':['najska.jpg'],
            'comment':'Self test comment',
            }  

        status = 201
        response = self.app_tester.post('/api/v1/red-flags', json=flag_data)
        self.assertEqual(response, status)


        


