from google.cloud import firestore

db = firestore.Client()

temp_ref = db.collection(u'temps').document(u'living_room')
temp_ref.set({
   u'time': 17222272,
   u'temp': 19.5,
   u'location': u'Living Room'
})

