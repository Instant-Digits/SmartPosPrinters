from firebase import Firebase
from functions import configPrinters
from uuid import getnode as get_mac
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting
import time

config = {
        "apiKey": "AIzaSyANL3DLuQ9IZxN5sOjxODg4IoPuXQm6UxM",
        "authDomain":  "aidrevs-test.firebaseapp.com",
        "databaseURL":  "https://aidrevs-test-default-rtdb.asia-southeast1.firebasedatabase.app",
        "storageBucket": "aidrevs-test.appspot.com"
    }
firebasecon = Firebase(config)
db = firebasecon.database()

printers={}

mac = get_mac()
metaData=db.child('/Printers/'+str(mac)).get().val();
try :
        metaData= dict(metaData)
except TypeError:
        print ('Invalued config')


def configurate ():
    global metaData, printers
    printers={}    
    print('searching for printers')

    while (True):
        printers = configPrinters(metaData)
        if(printers):
            break
        time.sleep(1)
    print('Configuration Success')
   
configurate()

if ('thermalPrinter' in printers):
    def listener(message):
        data=message["data"]        
        if(data and len(printers)>0):            
            try :
                setThermalPrinting(printers['thermalPrinter'],metaData,data)                
            except :
                print('printer error')
                configurate()
                setThermalPrinting(printers['thermalPrinter'],metaData,data)
            db.child(metaData['firmID']+'/thermalPrint').remove()

    db.child(metaData['firmID']+'/thermalPrint').stream(listener)


if ('formPrinter' in printers):
    def listener(message):
        data=message["data"]        
        if(data and len(printers)>0):            
            try :
                setDotMatrixPrinting(printers['formPrinter'],metaData,data)
            except :
                print('printer error')
                configurate()
                setDotMatrixPrinting(printers['formPrinter'],metaData,data)
            db.child(metaData['firmID']+'/formPrint').remove()
    db.child(metaData['firmID']+'/formPrint').stream(listener)

