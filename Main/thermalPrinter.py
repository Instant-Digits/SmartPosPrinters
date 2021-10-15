from functions import currencyFormater

def setThermalPrinting(printer,  printingHeader,printData):     

    #Header
    printer.align('center')
    printer.bold()
    printer.text(printingHeader['name'])
    printer.lf()
    printer.bold(False)


    printer.text(printingHeader['address'])
    printer.lf()	
    printer.text(printingHeader['tp'])
    printer.lf()
    
    printer.lf()
    printer.align('left')
    printer.text(printData['date'] +'@'+printData['time']+' -- '+printData['name']+' -- '+printData['type'])
    printer.lf()


    #print Bill
    for (key, value) in printData['itemList'].items():
        printer.align('left');
        printer.text(value['make']+' '+value['item'] );
        printer.lf();
        printer.align('right')
        printer.text ("{:<1} {:<15} {right_aligned:>12} ".format(' ', 
                str(value['quantity']) +' x Rs.'+currencyFormater(value['unitPrice']), 
                right_aligned='Rs.'+currencyFormater(value['unitPrice']*value['quantity'])
                ));
        printer.lf()
    printer.text ('')
    printer.lf()
    printer.text ("{:<1} {:<10} {:<14}".format('','TOTAL','Rs. '+currencyFormater(printData['total'])))
    printer.lf();
    
    printer.lf()
    printer.lf()
    printer.align('center')
    printer.text(' ------------------------------------------ ')
    printer.lf()
    printer.invert()
    printer.text(' POWERED BY INSTANT DIGITS (PVT) LTD ')
    printer.lf()
    printer.text(' Call us on 071 999 2075 ')
    printer.lf()
    printer.invert(False)


    printer.lf()
    printer.lf()
    printer.lf()
    printer.lf()
        
    printer.text('\x1dV\x00')




# printer = getUSBPrinter()(idVendor=0x0483,  # USB vendor and product Ids for Bixolon SRP-350plus
#                   idProduct=0x5743,  # printer
#                   inputEndPoint=0x82,
#                   outputEndPoint=0x01)
