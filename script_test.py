import time
import random
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

    df["TEMP_PQUENTE"].iloc[0] = df["TEMP_PQUENTE"].iloc[0] * random.randint(8, 12) / 10
    df["TEMP_PFRIO"].iloc[0] = df["TEMP_PFRIO"].iloc[0] * random.randint(8, 12) / 10
    df["IBAT"].iloc[0] = df["IBAT"].iloc[0] * random.randint(8, 12) / 10
    df["IGER"].iloc[0] = df["IGER"].iloc[0] * random.randint(8, 12) / 10
    df["IRRAD_LDR"].iloc[0] = df["IRRAD_LDR"].iloc[0] * random.randint(8, 12) / 10
    df["IRRAD_UV"].iloc[0] = df["IRRAD_UV"].iloc[0] * random.randint(8, 12) / 10
    df["ROT"].iloc[0] = df["ROT"].iloc[0] * random.randint(8, 12) / 10
    df["TEMP_REFLETOR"].iloc[0] = df["TEMP_REFLETOR"].iloc[0] * random.randint(8, 12) / 10
    df["VBAT"].iloc[0] = df["VBAT"].iloc[0] * random.randint(8, 12) / 10
    df["VGER"].iloc[0] = df["VGER"].iloc[0] * random.randint(8, 12) / 10

    dictionary = dict(zip(df.keys(), df.values[0]))
    doc_ref = db.collection(u'Usina').document(u'teste')
    doc_ref.set(dictionary)

    time.sleep(4)



