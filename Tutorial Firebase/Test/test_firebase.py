import pyrebase
from datetime import date, datetime
config = {
  "apiKey": "apiKey",
  "authDomain": "eventos.firebaseapp.com",
  "databaseURL": "https://eventos-1edcd-default-rtdb.firebaseio.com/",
  "storageBucket": "local"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = {"Evento":"Seminario","D":3,"M":2,"Y":2020}
db.child("Eventos").push(data)

mes = str(date.today().month)
mes = "2"

eventos= db.child(mes).get()
if isinstance(eventos.each(), list):
	for user in eventos.each():
		a=str(user.val())
		b= a.split()
		print("Titulo: "+b[3][1:-2]+", Día: "+ b[1][:-1])	
else:
	print("No existen eventos ingresados este mes")
	
	






