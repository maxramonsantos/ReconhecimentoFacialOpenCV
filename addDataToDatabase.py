import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://sitemadereconhecimentfacial-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
#print("deu certoooooooooooooo")

data = {
    "03102003":
        {
            "name": "Max Ramon",
            "major": "Eng. de Software",
            "starting_year": 2021,
            "total_attendance":6,
            "standing": "B",
            "year":4,
            "last_attendance_time": "2024-06-30 00:54:34"
        },
    "27062003":
        {
            "name": "Manoel Gomes (caneta azul)",
            "major": "Produtor musical",
            "starting_year": 2019,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-05-30 00:54:34"
        },
    "28062003":
        {
            "name": "Herminio Pedro",
            "major": "Eng. de Software",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-08-30 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)