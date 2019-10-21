import serial
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyrebase

    
def notifyemail(value):
    msg = MIMEMultipart()
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("abhiram.akas", "pushpaihatetears123") 
    msg['From'] = "abhiram.akas@gmail.com"
    msg['To'] = "s.ritika1705@gmail.com"
    msg[''] = 'Electricity Usage - '
    body ='''
    HEY USER!
        You have Electric Usage of \n\n\n
        
        
    ''' + value +'''\n\n\n
    Have a Great Day!
    
    '''
    msg.attach(MIMEText(body,'html'))
    s.sendmail("abhiram.akas@gmail.com","manishakri668@gmail.com",msg.as_string())
    
    print("notified")
    
config = {
    "apiKey": "AIzaSyARg6Noc__Pzg9d6iP32wyUmdl5M3OfNz0",
    "authDomain": "powerodata.firebaseapp.com",
    "databaseURL": "https://powerodata.firebaseio.com",
    "projectId": "powerodata",
    "storageBucket": "powerodata.appspot.com",
    "messagingSenderId": "405872297496",
    "appId": "1:405872297496:web:e6a25cea70f9ec8b96e56d",
    "measurementId": "G-4Z042SWGFH"
  };
firebase = pyrebase.initialize_app(config)
db = firebase.database()

print('Set up done')
ser = serial.Serial('COM4', 9600)
time.sleep(2)
data =[]                       # empty list to store the data
for i in range(10):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    #flt = float(string)        # convert string to float
    print(string)
    
    db.push({str(i):str(string)})
    #data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds
    notifyemail(string)



ser.close()

'''
var firebaseConfig = {
    apiKey: "AIzaSyARg6Noc__Pzg9d6iP32wyUmdl5M3OfNz0",
    authDomain: "powerodata.firebaseapp.com",
    databaseURL: "https://powerodata.firebaseio.com",
    projectId: "powerodata",
    storageBucket: "powerodata.appspot.com",
    messagingSenderId: "405872297496",
    appId: "1:405872297496:web:e6a25cea70f9ec8b96e56d",
    measurementId: "G-4Z042SWGFH"
  };'''