import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
firebase=firestore.client()
