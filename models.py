from google.appengine.ext import ndb

class User_info(ndb.Model):
    username = ndb.StringProperty(required=True)
    phone_num = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
