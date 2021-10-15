from firebase import Firebase
from functions import configPrinters
from uuid import getnode as get_mac
from dotMatrixPrinter import setDotMatrixPrinting
from thermalPrinter import setThermalPrinting


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
    printers = configPrinters(metaData)
except TypeError:
    print ('Invalued config')

if ('thermalPrinter' in printers):
    def listener(message):
        data=message["data"]
        if(data):
            db.child(metaData['firmID']+'/thermalPrint').remove()
            setThermalPrinting(printers['thermalPrinter'],metaData,data)

    db.child(metaData['firmID']+'/thermalPrint').stream(listener)


if ('formPrinter' in printers):
    def listener(message):
        data=message["data"]
        if(data):
            db.child(metaData['firmID']+'/formPrint').remove()
            setDotMatrixPrinting(printers['formPrinter'],metaData,data)

    db.child(metaData['firmID']+'/formPrint').stream(listener)

