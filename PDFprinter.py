from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)

can.setFont("Helvetica", 11)
can.drawString(70, 570, "NAME")
can.drawString(135, 570, ": MURUKANDY H/W")

can.drawString(70, 555, "PHONE")
can.drawString(135, 555, ": 0776778048")

can.drawString(70, 540, "ADDRESS")
can.drawString(135, 540, ": KILINOCHCHI")


can.drawString(370, 570, "Date")
can.drawString(430, 570, ": 22/02/2022 08:12 AM")

can.drawString(370, 555, "Invoice No.")
can.drawString(430, 555, ": 12-21-100")

can.drawString(370, 540, "Issued by")
can.drawString(430, 540, ": SHAGANAN")


can.setFont("Helvetica", 10)

can.drawString(37, 470, "{:^12}".format( '1'))
can.drawString(80, 470, "MYROS BRAND HAND HACKSAW BLADES 18TPI")
can.drawString(330, 470, "{:^18}".format( '1,000'))
can.drawString(390, 470, "{:^27}".format( '10,000'))
can.drawString(480, 470, "{:>24}".format( '100,000.00'))

can.drawString(37, 455, "{:^12}".format( '11'))
can.drawString(80, 455, "MYROS BRAND HAND HACKSAW BLADES 18TPI")
can.drawString(330, 455, "{:^18}".format( '500'))
can.drawString(390, 455, "{:^27}".format( '1,000'))
can.drawString(480, 455, "{:>24}".format( '300,000.00'))

can.drawString(37, 440, "{:^12}".format( '25'))
can.drawString(80, 440, "MYROS BRAND HAND HACKSAW BLADES 18TPI")
can.drawString(330, 440, "{:^18}".format( '50'))
can.drawString(390, 440, "{:^27}".format( '1,000'))
can.drawString(480, 440, "{:>24}".format( '30,000.00'))

can.setFont("Helvetica", 13)
can.drawString(450, 210, "{:>24}".format( '100,000.00'))








can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("template.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()