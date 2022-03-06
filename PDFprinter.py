from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import os
from functions import currencyFormater
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def setPDFInvoicePrinter (printer,printingHeader,printData ):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    cusPhone = printData['namePhone'] if ('namePhone' in printData and printData['namePhone']) else '--'
    cusAdress =  printData['nameAddress'] if 'nameAddress' in printData else '--' 

    if int(printData['balance'])>0 :
        invType = 'A/C'+' '+printData['type'] 
    elif (int(printData['balance'])==0 and printData['type'] in ['Sales', 'Sales_Saved']):  
        invType = 'Cash'+' '+printData['type']
    else:
        invType =printData['type']

    can.setFont("Helvetica", 11)
    can.drawString(70, 570, "NAME")
    can.drawString(135, 570, ": "+printData['name'].upper())

    can.drawString(70, 555, "PHONE")
    can.drawString(135, 555, ": "+cusPhone)

    can.drawString(70, 540, "ADDRESS")
    can.drawString(135, 540, ": "+cusAdress)

    can.setFont("Helvetica", 11)
    can.drawString(370, 578, "Date")
    can.drawString(430, 578, ": "+printData['date']+' '+ printData['time'][0:5] +' '+printData['time'][-2:])

    can.drawString(370, 563, "Invoice No.")
    can.drawString(430, 563, ": "+printData['invoiceSN'])

    can.drawString(370, 548, "Inv. Type")
    can.drawString(430, 548, ": "+invType.upper())

    can.drawString(370, 533, "Issued by")
    can.drawString(430, 533, ": "+printData['issuedby'])


   

    if (printData['type']=='Paid'):
        comment = "("+printData['comment']+')' if ('comment' in printData and  printData['comment'] and printData['comment']!='Nothing' ) else ' '
        can.setFont("Helvetica", 13)
        can.drawString(37, 460, "{:^12}".format( '1'))
        can.drawString(80, 460, 'A PAYMENT RECEIVED-CONFIRMATION' )
        can.drawString(340, 460,"{:^32}".format( printData['payMethod']))
        can.drawRightString(570, 460, currencyFormater(printData['total'])+'.00')
        can.setFont("Helvetica", 11)
        can.drawString(80, 444, comment )

        can.setFont("Helvetica", 13)
        can.drawRightString(565, 210, 'Rs. '+currencyFormater(float(printData['total']))+'0')
        

    else :
        can.setFont("Helvetica", 10)
        i=0
        for (key, value) in printData['itemList'].items():
            y=470-i*15
            i=i+1
            can.drawString(37, y, "{:^12}".format( str(i)))
            can.drawString(80, y, value['label'].upper() )
            can.drawString(330, y, "{:^18}".format( value['quantity']))
            can.drawRightString(470, y, currencyFormater(value['unitPrice'])+'.00')
            can.drawRightString(570, y,  currencyFormater(float(value['unitPrice'])*float(value['quantity']))+'0')

        can.setFont("Helvetica-Bold", 12)
        can.drawString(400, 257, "{:<18}".format( 'TOTAL'))
        can.drawRightString(570, 257,currencyFormater(float(printData['total']))+'0')

        can.drawString(400, 240, "{:<18}".format( 'PAID'))
        can.drawRightString(570, 240,'('+currencyFormater(float(printData['payAmount']))+'0)')
    
        can.setFont("Helvetica-Bold", 13)
        can.drawRightString(565, 210, 'Rs. '+currencyFormater(float(printData['balance']))+'0')

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("paymentTemp.pdf", "rb")) if (printData['type']=='Paid') else PdfFileReader(open("invoiceTemp.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    os.system('lp ./destination.pdf')


# from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.units import inch, mm, cm, pica
# from datetime import date, timedelta

# if __name__ == "__main__":
#     pdf = Canvas("output.pdf")
#     pdf.setFont('Helvetica', 9)

#     master_data = ...
#     start = ...
#     end = ...
#     company = ...
#     today = ...

#     lines = [
#         "Rechnungsdatum: "+'today',
#         "Leistungserbringung: "+ '',
#         "Leistungszeitraum: "+'start'+" - "+'end',
#         "Rechnungsnummer: "+'',
#         "Lieferantennummer: ",
#         "Zahlungsziel: " +str((date.today().replace(day=1) - timedelta(days=1)).day)+ " Tage",
#     ]
#     ys = [600,590,580,570,560,550]
#     width = pdf._pagesize[0]
#     padding = 10 * mm
#     for y, line in zip(ys, lines):
#         pdf.drawRightString(20, y, line)
#     pdf.save()