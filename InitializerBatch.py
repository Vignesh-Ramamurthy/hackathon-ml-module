import pandas as pd
pd.set_option("display.max_rows", 999)
pd.set_option('max_colwidth',100)
import numpy as np
from IPython.display import display
import Mongo as m

filepath = "emails\emails.csv"
# Read the data into a pandas dataframe called emails
emails = pd.read_csv(filepath)
headers = [header for header in emails.columns]
print("Successfully loaded {} rows and {} columns!".format(emails.shape[0], emails.shape[1]))
print(display(emails.head()))
print(emails.loc[0]["message"])

print(emails)
import email

def insert_value(dictionary, key, value):
    if key in dictionary:
        values = dictionary.get(key)
        values.append(value)
        dictionary[key] = values
    else:
        dictionary[key] = [value]
    return dictionary

def get_headers(df, header_names):
    headers = {}
    messages = df["message"]
    for message in messages:
        e = email.message_from_string(message)
        for item in header_names:
            header = e.get(item)
            insert_value(dictionary = headers, key = item, value = header) 
    print("Successfully retrieved header information!")
    return headers
header_names = ["Date", "Subject", "From", "To","cc","bcc","Message-ID"]    
headers = get_headers(emails, header_names)




def get_messages(df):
    messages = []
    for item in df["message"]:
        # Return a message object structure from a string
        e = email.message_from_string(item)    
        # get message body  
        message_body = e.get_payload()
        message_body = message_body.lower()
        messages.append(message_body)
    print("Successfully retrieved message body from e-mails!")
    return messages
msg_body = get_messages(emails)
emails["Message-Body"] = msg_body


def split_array_contents_by_comma(df,col):
    new_set= set()
    employeeList = df[col].values.tolist()
    for employeeUnSplit in employeeUnSplitList:
        if( (employeeUnSplit is None) or (len(employeeUnSplit) == 0)):
            continue
        employeeSplitList = employeeUnSplit.split(',')
        for employeeSplit in employeeSplitList:
            new_set.add(employeeSplit)
    return new_set





    



x_from = pd.DataFrame(headers["From"], columns = ["From"])
if "From" not in emails.columns:
    emails = pd.concat([emails, x_from], axis = 1, join = 'inner')

x_from = split_array_contents_by_comma(x_from,"From")

print("printing From employees")
print(len(x_from))

x_to = pd.DataFrame(headers["To"], columns = ["To"])

if "To" not in emails.columns:
    emails = pd.concat([emails, x_to], axis = 1, join = 'inner')
    emails['To'].replace('None', np.nan, inplace=True)
    emails["To"].fillna("dummy",inplace=True)

x_to = split_array_contents_by_comma(x_to,"To")





print("printing To employees")
print(len(x_to))


x_cc = pd.DataFrame(headers["cc"], columns = ["cc"])
if "cc" not in emails.columns:
    emails = pd.concat([emails, x_cc], axis = 1, join = 'inner')
    emails['cc'].replace('None', np.nan, inplace=True)
    emails["cc"].fillna("dummy",inplace=True)
x_cc = split_array_contents_by_comma(x_cc,"cc")






print("printing cc employees")
print(len(x_cc))




x_bcc = pd.DataFrame(headers["bcc"], columns = ["bcc"])
if "bcc" not in emails.columns:
    emails = pd.concat([emails, x_bcc], axis = 1, join = 'inner')
    emails['bcc'].replace('None', np.nan, inplace=True)
    emails["bcc"].fillna("dummy",inplace=True)
x_bcc = split_array_contents_by_comma(x_bcc,"bcc")




print("printing bcc employees")
print(len(x_bcc))


employees = list(set().union(x_from,x_to,x_cc,x_bcc))

x_msg_id = pd.DataFrame(headers["Message-ID"], columns = ["Message-ID"])
if "Message-ID" not in emails.columns:
    emails = pd.concat([emails, x_msg_id], axis = 1, join = 'inner')

x_subject = pd.DataFrame(headers["Subject"], columns = ["Subject"])
if "Subject" not in emails.columns:
    emails = pd.concat([emails, x_subject], axis = 1, join = 'inner')



print("printing a random email instance")
print(emails.loc[100])

NaN = np.NaN
emails["tagName"] = NaN



