import re
import os
import tabula
import PyPDF2


#function for list convert into string
def list_to_string(table):
    str1 = ''
    for ele in table:
        str1 += ele
    
    return str1


pdf_path = r"D:\invoice\invoice 3.pdf"

#extracting number of pages 
reader = PyPDF2.PdfFileReader(pdf_path)
no_of_pages = reader.getNumPages()

#extract the all data from pdf
pageObject = reader.getPage(no_of_pages-1)
extract_data = pageObject.extract_text()
print(extract_data)


#extracting the table data from pdf
table = tabula.read_pdf(pdf_path, pages= no_of_pages)
str4 = "Invoice Number : INZ-4313 and date is Feb 28, 2022"

#table list data convert in to string format
invoice_extract_data = ' '.join(str(e) for e in table)

#date and Invoice numbber extraction complete.
date = re.findall('[a-zA-Z]+\ +\d+\S+\ +\d+', invoice_extract_data)
invoice_number = re.findall('[a-zA-Z]+\-+\d+', invoice_extract_data)
# print(date, invoice_number)