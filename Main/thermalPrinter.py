from functions import currencyFormater

def setThermalPrinting(printer,  printingHeader,printData):     

    #Header
    printer.align('center')
    printer.bold()
    printer.text(printingHeader['name'].upper())
    printer.lf()
    printer.bold(False)

    if (int(printData['balance'])>0 and printData['type']=='Sales' ):
        invType = 'A/C'+' '+printData['type'] 
    elif (int(printData['balance'])==0 and printData['type']=='Sales' ):  
        invType = 'Cash'+' '+printData['type']
    else:
        invType =printData['type']


    printer.text(printingHeader['address'])
    printer.lf()	
    printer.text(printingHeader['tp'])
    printer.lf()
    printer.lf()
    printer.text('Invoice No :- '+printData['invoiceSN'])
    printer.lf()
    printer.bold()
    printer.lf()
    printer.align('left')
    printer.text("Name : "+printData['name'] )
    printer.lf()
    printer.text("Type : "+invType )
    printer.lf()
    printer.text("Date : "+printData['date'] +' Time : '+printData['time'])
    printer.lf()
    printer.lf()
    printer.bold(False)

   
    #print Bill
    if (printData['type']=='Paid'):
        
        printer.align('center')
        

        printer.text ("{:<1} {:<25} {:<14}".format('','PAYMENT METHOD',printData['payMethod']))        
        printer.lf()
        printer.lf()
        printer.bold()
        printer.text ("{:<1} {:<25} {:<14}".format('','RECEIVED AMOUNT','Rs. '+currencyFormater(printData['total'])))        
        printer.lf()
        printer.bold(False)
        printer.lf()
        printer.text ("{:<1} {:<25} {:<14}".format('','RECEIVED BY',printData['issuedby']))        
        printer.lf()
        printer.lf()
        printer.text('THANK YOU FOR YOUR PAYMENT !');
        printer.lf()
        
      

    else: 
        i=1
        for (key, value) in printData['itemList'].items():
            printer.align('left');
            printer.text(str(i)+'. '+value['label'] );
            i=i+1
            printer.lf();
            printer.align('right')
            printer.bold()
            printer.text ("{:<8} {:<2} {:<14} {right_aligned:>15}".format('Qts. : '+str(value['quantity']) , " ",
                    'x Rs.'+currencyFormater(value['unitPrice']), 
                    right_aligned='Rs. '+currencyFormater(float(value['unitPrice'])*float(value['quantity']))
                    ));
            printer.lf()
            printer.bold(False)
            printer.lf()
        printer.text ('')
        printer.bold()
        printer.lf()
        printer.text ("{:<1} {:<10} {:<14}".format('','TOTAL','Rs. '+currencyFormater(float(printData['total']))))
        printer.lf();
        printer.lf();
        printer.text ("{:<1} {:<10} {:<14}".format('','PAID','Rs. '+currencyFormater(float(printData['payAmount']))))
        printer.lf();
        printer.bold(False)
        printer.align('center')
        printer.lf() 
        printer.lf() 
        printer.bold()
        printer.text("Thank You!")
        printer.lf()
    
      
    printer.bold(False)
    printer.lf()
    printer.align('center')
    printer.text(' ------------------------------------------ ')
    printer.lf()
    printer.bold()
    printer.invert()
    printer.text('A WIRELESS SOLUTION BY INSTANT DIGITS (PVT) LTD')
    printer.lf()
    printer.text(' Call us on 077 677 8048 ')
    printer.lf()
    printer.bold(False)
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
