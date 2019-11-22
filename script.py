import time
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./helius-1983c-firebase-adminsdk-bkl2t-d8f9d3d1ef.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

while(True):
    df = pd.read_csv('./file.csv')
    df = df.round(3)
    dictionary = dict(zip(df.keys(), df.values[0]))
    doc_ref = db.collection(u'Usina').document(u'1')
    doc_ref.set(dictionary)

    time.sleep(10)



