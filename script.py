import time
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./helius-1983c-firebase-adminsdk-1uodv-f64849b92b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

while(True):
    df = pd.read_csv('./file.csv')
    df = df.round(3)
    dictionary = dict(zip(df.keys(), df.values[0]))
    doc_ref = db.collection(u'usinas').document(u'usina1')
    doc_ref.set(dictionary)

    time.sleep(10)



