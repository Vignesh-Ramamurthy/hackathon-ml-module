import pandas as pd
from pymongo import MongoClient
def updateDfToMongo(df,collectionName):
    client =  MongoClient("mongodb+srv://manojuser:manojuser@cluster0-2juvg.mongodb.net/test?retryWrites=true&w=majority")
    db = client['hackathon']
    collection = db[collectionName]
    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    # Insert collection
    collection.insert_many(data_dict)

def updateUserSchema(df,emailIdList):
    dictionary:dict = {}
    for emailId in emailIdList:
        resultDfTo = df[df['To']==emailId]
        resultDfCc = df[df['cc']==emailId]
        resultDfBcc = df[df['bcc']==emailId]
        vertical_stack = pd.concat([resultDfTo, resultDfCc,resultDfBcc], axis=0)
        dictionary[emailId] = vertical_stack['Message-ID'].values.tolist()
    client =  MongoClient("mongodb+srv://manojuser:manojuser@cluster0-2juvg.mongodb.net/test?retryWrites=true&w=majority")
    db = client['hackathon']
    collection = db['userSchema']
    collection.insert_many(dictionary)
    

    return

