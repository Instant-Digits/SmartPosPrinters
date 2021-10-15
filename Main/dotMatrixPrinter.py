from functions import currencyFormater

def setDotMatrixPrinting(printer,printingHeader,printData ):
    i=1
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
    printer.text ("{:<1} {:<6} {:<14}".format('','DATE',': '+printData['date'] +' @ ' +printData['time'].upper()))
    printer.lf()
    printer.text ("{:<1} {:<6} {:<14}".format('','NAME',': '+printData['name']))
    printer.lf()
    printer.text ("{:<1} {:<6} {:<14}".format('','TYPE',': '+printData['type']))
    printer.lf()


    printer.lf() 
    printer.text ("{:<1} {:^5} {:^30} {:^6} {:^4} {:^8} {:^6} {:^9}".format(
                ' ', 
                'NO',
                'DESCRIPTION', 
                'QTS.',
                'UNIT',
                'RATE',
                'DIS.',
                "AMOUNT"               
                ));
    printer.lf()    
    

    #print Bill
    
    for (key, value) in printData['itemList'].items():
        printer.align('left');
        printer.text ("{:<1} {:^5} {:<30} {:^6} {:^4} {:^8} {:^6} {:>9}".format(
                ' ', 
                i,
                value['make']+' '+value['item'] , 
                value['quantity'],
                'Nos',
                currencyFormater(value['unitPrice']),
                '0.00',
                currencyFormater(value['unitPrice']*value['quantity']),               
                ));
        printer.lf();
        i=i+1;

    printer.lf()  
    printer.text ("{:<1} {:^5} {:<25} {:^6} {:^4} {:^8} {:^8} {:>12}".format(
            ' ', 
            '',
            '' , 
            '',
            '',
            '',
            'TOTAL',
            'Rs. '+currencyFormater(printData['total']),               
            ));
    printer.lf();
    
    
    printer.lf()
    printer.lf()
    printer.align('center')
    printer.text(' ------------------------------------------------------ ')
    printer.lf()
    printer.text(' POWERED BY INSTANT DIGITS (PVT) LTD ')
    printer.lf()
    printer.text(' Call us on 071 999 2075 ')
    printer.lf()
    printer.lf()
    