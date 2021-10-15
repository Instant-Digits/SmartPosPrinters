from textwrap import wrap
from escpos.connections import getUSBPrinter


def currencyFormater (num):
    list = wrap(str(num)[::-1], 3)
    return ','.join(list)[::-1]

def configPrinters (configData):
    printers={}
    if ('config' in configData.keys()):
        printerConfig =configData['config']
        for (key, value) in printerConfig.items():
            try:
                printers[key] = getUSBPrinter()(idVendor=int(value['idVendor'],16),  # USB vendor and product Ids for Bixolon SRP-350plus
                                                idProduct=int(value['idProduct'],16),  # printer
                                                inputEndPoint=int(value['inputEndPoint'],16),
                                                outputEndPoint=int(value['outputEndPoint'],16))
            except RuntimeError:
                print (key+' NOT DETECTED')
        return printers
    return (configData)

#print (currencyFormater(12345678))