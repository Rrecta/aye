from google.appengine.ext import ndb

class Event(ndb.Model):
    owner = ndb.StringProperty(required=True)
    host = ndb.StringProperty(required=True)
    guest = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)

class CrashCouchUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()
  friend = ndb.StringProperty()
    
