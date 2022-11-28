from email.message import EmailMessage
import smtplib
import pandas as pd

#User Login Details
password = 'Enter Password'
from_addr = 'Enter email Address'

#Excel file path
df = pd.read_excel(r"D:\use_case\use case demo.xlsx")


to_addr = df['Email'].values
cc = df['Cc'].values
subject = df['Subject']
attachment_path_1 = df['Attachment 1']
attachment_path_2 = df['Attachment 2']
attachment_path_3 = df['Attachment 3']

zipped = zip(to_addr,cc,subject,attachment_path_1, attachment_path_2, attachment_path_3)

for(a,b,c,d,e,f) in zipped:

    msg = EmailMessage()
    files = [(r'{}'.format(d))]
    files = [(r'{}'.format(e))]
    files = [(r'{}'.format(f))]

    for file in files:
        with open(file, 'rb') as p:
            file_data = p.read()

        msg['From'] = from_addr
        msg['To'] = a
        msg['Cc'] = b
        msg['Subject'] = c
        msg.set_content(f"{c}")
        msg.add_attachment(file_data, 'Application', 'octet-stream', filename = "{}".format(d))
        msg.add_attachment(file_data, 'Application', 'octet-stream', filename="{}".format(e))
        msg.add_attachment(file_data, 'Application', 'octet-stream', filename="{}".format(f))

        rctp = b.split(',') + [a]
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_addr, password)
            smtp.send_message(msg)

        print(f'Send to {a}')

print('All mail sent')
