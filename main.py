import webapp2
import jinja2
import os
from models import Event, CrashCouchUser
from google.appengine.api import users
import twilio
from twilio.rest import Client



the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def send_sms():
    account_sid = 'ACeb53036e0973b4d06165a904bb49b64a'
    auth_token = '36fb7e99c2b6eb9fc699a7f9892e210c'
    client = Client(account_sid, auth_token)
                
    message = client.messages \
                    .create(
                        body="hello this crash couch we are watching you and it seems you have not signed up for our website yes sir",
                        from_='+18317848769',
                        to='+18317741358'
                                 )
    print(message.sid)


def checkLoggedInAndRegistered(request):
    # Check if user is logged in
    print("in checkLoggedInAndRegistered")
    
    user = users.get_current_user()
        
    if not user: 
        print("User not logged in")
        request.redirect("/login")
        return
    
    # Check if user is registered
       
    email_address = user.nickname()
    registered_user = CrashCouchUser.query().filter(CrashCouchUser.email == email_address).get()
    
    if not registered_user:
         print("user not registered")
         request.redirect("/register")
         return 
    

class HomeHandler(webapp2.RequestHandler):
    
    
    
    def get(self): 
        print("In homeHandler***************************")
        checkLoggedInAndRegistered(self)
        
        the_variable_dict = {
            "logout_url":  users.create_logout_url('/')
        }
        
        welcome_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(welcome_template.render(the_variable_dict))

    def post(self):
        checkLoggedInAndRegistered(self)
        
        send_sms()
        
        user = users.get_current_user()
        
        event = Event(
            owner=user.nickname(),
            host=self.request.get('host'), 
            guest=self.request.get('guest'),
            date=self.request.get('date'),
        )
        event_key = event.put()
        

        
        
            



        self.response.write("Meme created: " + str(event_key) + "<br>")
        self.response.write("<a href='/allmemes'>All memes</a> | ")
        self.response.write("<a href='/usermemes'>My memes</a>")


class AllMemesHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        
        
        all_events = Event.query().fetch()
        
        the_variable_dict = {
            "all_events": all_events
        }
        
        all_memes_template = the_jinja_env.get_template('templates/all_memes.html')
        self.response.write(all_memes_template.render(the_variable_dict))

class UserMemesHandler(webapp2.RequestHandler):
    def get(self):
        checkLoggedInAndRegistered(self)
        
        user = users.get_current_user()
        email_address = user.nickname()
        
        user_events = Event.query().filter(Event.owner == email_address).fetch()
    
        the_variable_dict = {
            "user_events": user_events
        }
        
        user_memes_template = the_jinja_env.get_template('templates/user_memes.html')
        self.response.write(user_memes_template.render(the_variable_dict))
   
        

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        
        login_template = the_jinja_env.get_template('templates/login.html')
        the_variable_dict = {
            "login_url":  users.create_login_url('/')
        }
        
        self.response.write(login_template.render(the_variable_dict))
        

class RegistrationHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        print("in registrationhandler")
        registration_template = the_jinja_env.get_template('templates/registration.html')
        the_variable_dict = {
            "email_address":  user.nickname()
        }
        
        self.response.write(registration_template.render(the_variable_dict))
    
    def post(self):
        user = users.get_current_user()
        
        #Create a new CSSI User in our database
        
        crash_couch_user = CrashCouchUser(
            first_name=self.request.get('first_name'), 
            last_name =self.request.get('last_name'), 
            email=user.nickname(),
            friend=self.request.get('friend')
        )
        
        crash_couch_user.put()
        
        self.response.write('Thanks for signing up, %s! <br><a href="/">Home</a>' %
        crash_couch_user.first_name)
        
        
        
        
                  
    
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/allmemes', AllMemesHandler), 
    ('/usermemes', UserMemesHandler), 
    ('/login', LoginHandler),
    ('/register', RegistrationHandler)
], debug=True)