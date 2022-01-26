from textwrap import wrap
from escpos.connections import getUSBPrinter
import time


def currencyFormater (num):
    desimalIndex= str(num).find('.')
    if desimalIndex>-1:
        list = wrap(str(num)[desimalIndex-1::-1], 3)
        return ','.join(list)[::-1]+str(num)[desimalIndex:desimalIndex+3] 
    list = wrap(str(num)[::-1], 3)
    return ','.join(list)[::-1]




def configPrinter (printerInfo, name='Printer', timeOut=5):
    timeStart = time.time()
    timeOut=timeOut*60
    while (True):
        try:
            printer = getUSBPrinter()(idVendor=int(printerInfo['idVendor'],16),  # USB vendor and product Ids for Bixolon SRP-350plus
                                            idProduct=int(printerInfo['idProduct'],16),  # printer
                                            inputEndPoint=int(printerInfo['inputEndPoint'],16),
                                            outputEndPoint=int(printerInfo['outputEndPoint'],16))
            print (name+' DETECTED')
            return printer
        except RuntimeError:
            print (name+' NOT DETECTED')
            print ('Waiting For '+name)
            time.sleep(5)
            if (time.time()>timeStart+timeOut):
                print ("waiting timeout for printer Search")
                return False
            

#print (currencyFormater('12345.50000'))