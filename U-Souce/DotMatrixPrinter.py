from firebase import Firebase
from functions import currencyFormater
from uuid import getnode as get_mac

config = {
        "apiKey": "AIzaSyANL3DLuQ9IZxN5sOjxODg4IoPuXQm6UxM",
        "authDomain":  "aidrevs-test.firebaseapp.com",
        "databaseURL":  "https://aidrevs-test-default-rtdb.asia-southeast1.firebasedatabase.app",
        "storageBucket": "aidrevs-test.appspot.com"
    }
firebasecon = Firebase(config)
db = firebasecon.database()

mac = get_mac()
print(mac)

def getConfigurationData (mac):
    configData=db.child('/Printers/'+str(mac)).get().val();
    configData= dict(configData)
    if ('config' in configData.keys()):
        printerConfig =configData['config']
        for (key, value) in printerConfig.items():
            for (idName, idValue) in value.items():
                print((idName, idValue))
    return (dict(configData))

metaData = getConfigurationData (mac)
printerConfig =metaData['config']
hex_s =  printerConfig['formPrinter']['idProduct']
a = int(hex_s,16)

print(0x0046==a)


print (printerConfig)


# printerData= db.child('test1/Printer').get().val();
# printerData= dict(printerData);
# printingHeader=printerData['PrintingDataHeader'];

#printData= db.child('test1/thermalPrint').get().val();

def PrinterJob(printData):
    for (key, value) in printData['itemList'].items():
        print(value['make']+' '+value['item'] );
        print ("{:<1} {:<15} {right_aligned:>12} ".format(' ', 
                str(value['quantity']) +' x Rs.'+currencyFormater(value['unitPrice']), 
                right_aligned='Rs.'+currencyFormater(value['unitPrice']*value['quantity'])
                ));
    print ('')
    print ("{:<1} {:<14} {:<10}".format('','TOTAL','Rs. '+currencyFormater(printData['total'])))

def listener(message):
	data=message["data"]
	if(data):
		db.child('test1/thermalPrint').remove()
		PrinterJob(data)
		



#db.child('test1/thermalPrint').stream(listener)


# left_aligned = "Left Align"
# center = "Centered"
# right_aligned = "Right Align"
# print("{left_aligned:<15}{center:^10}{right_aligned:>15}".format(
# left_aligned=left_aligned,
# center=center,
# right_aligned=right_aligned))

