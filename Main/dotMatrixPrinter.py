from functions import currencyFormater

def setDotMatrixPrinting(printer,printingHeader,printData ):
        lineNo =1
        i=1
    #Header
#     printer.align('center')
#     printer.bold()
#     printer.text(printingHeader['name'])
#     printer.lf()
#     printer.bold(False)


#     printer.text(printingHeader['address'])
#     printer.lf()	
#     printer.text(printingHeader['tp'])
#     printer.lf()
    
#     printer.lf()
#     printer.align('left')
#     printer.text ("{:<1} {:<6} {:<14}".format('','DATE',': '+printData['date'] +' @ ' +printData['time'].upper()))
#     printer.lf()
#     printer.text ("{:<1} {:<6} {:<14}".format('','NAME',': '+printData['name']))
#     printer.lf()
#     printer.text ("{:<1} {:<6} {:<14}".format('','TYPE',': '+printData['type']))
#     printer.lf()


#     printer.lf() 
#     printer.text ("{:<1} {:^5} {:^30} {:^6} {:^4} {:^8} {:^6} {:^9}".format(
#                 ' ', 
#                 'NO',
#                 'DESCRIPTION', 
#                 'QTS.',
#                 'UNIT',
#                 'RATE',
#                 'DIS.',
#                 "AMOUNT"               
#                 ));
#     printer.lf()    
    

    #print Bill

        # while (lineNo<50):
        #         printer.align('left');
        #         printer.text ('Line No : '+str(lineNo))
        #         printer.lf();
        #         lineNo=lineNo+1
        printer.align('left');
        
        while (lineNo<47):
                if lineNo==1: 
                        printer.text ("{:<1}{:<7} {:<19} {:^8} {:<3} {:>1}  {:>34}".format(      
                                        '',
                                       '',
                                        '', 
                                       '',
                                        '',
                                        '',
                                       'PRINTED ON : '+  printData['printedOn']           
                                        ));
                        printer.lf();
                        lineNo=lineNo+1

                elif (lineNo==5):
                        printer.text ("{:<1}{:<7} {:<29} {:^8} {:<3} {:>6} {:^3} {:^6} {:>10}".format(      
                                        '',
                                        'NAME',
                                        printData['name'].upper(), 
                                       '',
                                        '',
                                        '',
                                        '',
                                       '', '',              
                                        ));
                        printer.lf();
                        lineNo=lineNo+1 
                        printer.text ("{:<1}{:<7} {:<29} {:^8} {:<3} {:>6} {:^3} {:^6} {:>10}".format(      
                                        '','TYPE',printData['type'].upper(),'','','','','','',                
                                        ));
                        printer.lf();
                        lineNo=lineNo+1
                        printer.text ("{:<1}{:<7} {:<29} {:^8} {:<3} {:>6} {:^3} {:^6} {:>10}".format(      
                                        '',
                                        'DATE',
                                        printData['date'] , 
                                       '',
                                        '',
                                        '',
                                        '','',
                                       printData['invoiceSN'],               
                                        ));
                        printer.lf();
                        lineNo=lineNo+1
                        printer.text ("{:<1}{:<7} {:<29} {:^8} {:<3} {:>6} {:^3} {:^6} {:>10}".format(      
                                        '',
                                        'TIME',
                                        printData['time'], 
                                       '',
                                        '',
                                        '',
                                        '','',
                                       '',               
                                        ));
                        printer.lf();
                        lineNo=lineNo+1
                elif (lineNo==9) :
                        printer.text ("{:<1}{:<7} {:<29} {:^8} {:<1} {:<11}  {:^6} {:>10}".format(      
                                        '',
                                        '',
                                        '', 
                                       '',
                                        '',
                                        printData['issuedby'],
                                        '',
                                       '',               
                                        ));
                        printer.lf();
                        lineNo=lineNo+1 

                elif ( lineNo==15):
                        i=1
                        for (key, value) in printData['itemList'].items():                                
                                printer.text ("{:<1}{:<4} {:<32} {:^8} {:<3} {:>6} {:^3} {:^6} {:>10}".format(      
                                        '',
                                        i,
                                        value['make']+' '+value['item'] , 
                                        value['quantity'],
                                        'Nos',
                                        currencyFormater(value['unitPrice']),
                                        '%','0.00',
                                        currencyFormater(float(value['unitPrice'])*float(value['quantity'])),               
                                        ));
                                printer.lf();
                                lineNo=lineNo+1                                
                                i=i+1;
                elif ( lineNo==40):#40
                        printer.text ("{:<9}{:<10} {:<26} {:<3} {:>6} {:^9} {:>10}".format(      
                                        '',
                                        '',
                                        '',                                        
                                        '',
                                        '',
                                        'TOTAL (Rs)',
                                       currencyFormater(float(printData['total'])),               
                                        ));
                        printer.lf();
                        lineNo=lineNo+1                        
              
                else:
                        printer.lf();
                        lineNo=lineNo+1
        printer.text('\f')
        return
    
#    printer.text ("{:<1} {:^5} {:<25} {:^6} {:^4} {:^8} {:^8} {:>12}".format(
#             ' ', 
#             '',
#             '' , 
#             '',
#             '',
#             '',
#             'TOTAL',
#             'Rs. '+currencyFormater(printData['total']),               
#             ));
    
    
     
#     printer.lf()
#     printer.lf()
#     printer.align('center')
#     printer.text(' ------------------------------------------------------ ')
#     printer.lf()
#     printer.text(' POWERED BY INSTANT DIGITS (PVT) LTD ')
#     printer.lf()
#     printer.text(' Call us on 071 999 2075 ')
#     printer.lf()
#     printer.lf()
    