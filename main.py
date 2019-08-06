import webapp2
import jinja2
import os
from models import User_info


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def run_query(username, phone_num, email):
    user_info = (user_name = username, phone_number = phone_num, user_email = email)
    user_info_key = user_info.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(user_info_key)
    
class TestQueryHandler(webapp2.RequestHandler):
    def get(self):
        run_query("Huuurrrrahhh", "Wooooooot", "coding")    
        


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/showmeme', ShowMemeHandler),
    ('/testquery', TestQueryHandler),



