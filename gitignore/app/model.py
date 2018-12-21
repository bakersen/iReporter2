import random
import datetime

class Incident:
    def __init__(self, id, createOn, createBy, type, location, status, images, videos, comment):
        self.id = random.int(1000, 1000000)
        self.createOn = datetime.datetime.today().strftime('%Y-%m-%d')
        self.createdBy = createdBy
        self.location = location
        self.status = status
        self.images = []
        self.comment = comment

class User:
    def __init__(self, firstname, lastname, othernames, email, phonenumber, username, registered, isAdmin):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames,
        self.email = email
        self.phonenumber = phonenumber
        self.username = username
        self.registered = datetime.datetime.today().strftime('%Y-%m-%d')
        self.isAdmin





