from twilio.rest import Client



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


    