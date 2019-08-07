from google.appengine.ext import ndb

class Event(ndb.Model):
    line1 = ndb.StringProperty(required=True)
    line2 = ndb.StringProperty(required=True)
    owner = ndb.StringProperty(required=True)
    img_choice = ndb.StringProperty(required=False)

class CrashCouchUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()
    
