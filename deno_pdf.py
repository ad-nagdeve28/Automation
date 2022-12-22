import PyPDF2
import re
import os 

files_path = r"D:\invoice"
i = 0
for file_name in os.listdir('D:\invoice'):

    #data extraction from pdf files
    pdf_path = open(r'D:\invoice\\'+ file_name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_path)
    page_count = read_pdf.getNumPages()
    pages = read_pdf.getPage(page_count - 1)
    page_content = pages.extract_text()
    # page_content = page_content.replace('\n', '')
    # print(page_content+"\n")

    
    #sample date's 
    date = "Jan 31, 2023"
    
    #date extraction
    date1 = re.findall('[a-zA-Z]+\ +\d+\S+\ +\d+', date)
    # print(date1)
    date2 = re.findall("\d+\/\d+\/\d+",page_content)
    date3 = re.findall("\d+\s+\S+\s+\d+", page_content)
    date4 = re.findall("\d+\-+\S+\-+\d+", page_content)
    
    #extracted invoice number 
    invoice_number = re.findall('[a-zA-Z]+\-+\d+', page_content)
    
    #extracted mail address
    extract_mail = re.findall("[a-zA-Z0-9]+@+[a-zA-Z]+.+[a-zA-Z]+",page_content)
    emails = list(dict.fromkeys(extract_mail))
    
    #check weather which format is for date 
    if(date1 == '' or date2 == '' or date3 == '' or date4 == ''):
        pass
    elif(date1 != '' or date2 != '' or date3 != '' or date4 != ''):
        extract_date = date1
        extract_date = date2
        extract_date = date3
        extract_date = date4
    else:
        extract_date = "No Date found in invoice..!"
        
        
    extract_num1 = re.findall("\+\d+\s+\(\d+\)\s+\d+\-\d+", page_content)
    extract_num2 = re.findall("\+\d+\s+\(\d+\)\s+\d+\s+\d+",page_content)

    final_num = ''.join(extract_num1)
    #Extracted Result
    print(file_name + ":\n")
    if (extract_date != ''):
        print(','.join(extract_date))
    else:
        print("No Date found in Invoice")
    
    if (invoice_number != ''):
        print(','.join(invoice_number))
    else:
        print("No Date found in Invoice")
        
    if (emails != ''):
        print(', '.join(emails))
    else:
        print("No Date found in Invoice")

    if (extract_num1 == ''):
        print("No Date found in Invoice")
    else:
        print(extract_num1)
            

    print('\n')