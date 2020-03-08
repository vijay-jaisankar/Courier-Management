from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['DEBUG']=True
app.config['TESTING'] = False

# Location of mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 

# Port that the e-mail is sent through
app.config['MAIL_PORT'] = 465

# For security purposes
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Same value as overall debug
# app.config['MAIL_DEBUG']= True  

# Self-explanatory
app.config['MAIL_USERNAME'] = 'sender@gmail.com'
app.config['MAIL_PASSWORD'] = 'SenderPwd'

# Will add senser sepcified as 'From'
app.config['MAIL_DEFAULT_SENDER'] = ('Sender','sender@gmail.com')

# For protection purposes
app.config['MAIL_MAX_EMAILS'] = None 

# Same as testing value
# app.config['MAIL_SUPPRESS_SEND'] = False

# Converts file name specified into ASCII 
app.config['MAIL_ASCII_ATTACHMENTS'] = False


mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hey There',sender='sender@gmail.com',recipients=['recipient@gmail.com'])
    msg.html = '<b>This is a test e-mail</b>'	# change this
    
    with app.open_resource('bird1.png') as bird:	# for attachment ( Demonstrative purposes only)
        msg.attach('bird1.png','image/png', bird.read())

    mail.send(msg)

    

    return 'Message has been sent'

"""
@app.route('/bulk')
def bulk():
    users = [{'name': 'recepientName', 'email': 'recipient@gmail.com',}]

    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk!', recipients = [user['email']])
            msg.body = 'Hello!'
            conn.send(msg)           
"""




if __name__ == '__main__':
    app.run()



    
