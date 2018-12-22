import random
import datetime

class Incident:
    def __init__(self, id, createdOn, createdBy, type, location, status, images, videos, comment):
        self.id = random.randint(1000, 1000000)
        self.createdOn = datetime.datetime.today().strftime('%Y-%m-%d')
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.status = status
        self.images = []
        self.videos = []
        self.comment = comment
    
    def converts_json(self):
        return {
            'id':self.id, 
            'createdOn': self.createdOn, 
            'createBy': self.createdBy,
            'type': self.type,
            'location': self.location,
            'status': self.status,
            'Images':self.images,
            'Videos':self.videos,
            'comment':self.comment
            }

class User:
    def __init__(self, id, firstname, lastname, othernames, email, phonenumber, username, registered, isAdmin):
        self.id = random.randint(2000, 2000000)
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames,
        self.email = email
        self.phonenumber = phonenumber
        self.username = username
        self.registered = datetime.datetime.today().strftime('%Y-%m-%d')
        self.isAdmin = isAdmin
    
    def converts_json(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othernames': self.othernames,
            'email':self.email,
            'phonenumber': self.phonenumber,
            'usernamer': self.username,
            'registered': self.registered,
            'isAdmin': self.isAdmin
        }





