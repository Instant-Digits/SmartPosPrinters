from firebase import Firebase
from functions import currencyFormater

config = {
        "apiKey": "AIzaSyANL3DLuQ9IZxN5sOjxODg4IoPuXQm6UxM",
        "authDomain":  "aidrevs-test.firebaseapp.com",
        "databaseURL":  "https://aidrevs-test-default-rtdb.asia-southeast1.firebasedatabase.app",
        "storageBucket": "aidrevs-test.appspot.com"
    }
firebasecon = Firebase(config)
db = firebasecon.database()

printerData= db.child('test1/Printer').get().val();
printerData= dict(printerData);
printingHeader=printerData['PrintingDataHeader'];

printData= db.child('test1/print').get().val();

for (key, value) in printData['itemList'].items():
    print(value['make']+' '+value['item'] );
    print ("{:<3} {:<15} {:<10} ".format(' ', 
            str(value['quantity']) +' x Rs.'+currencyFormater(value['unitPrice']), 
            'Rs.'+currencyFormater(value['unitPrice']*value['quantity'])
            ));

print ('')
print ("{:<2} {:<14} {:<10}".format('','TOTAL','Rs. '+currencyFormater(printData['total'])))

