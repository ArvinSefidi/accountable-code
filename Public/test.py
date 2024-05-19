from firebase import firebase

myDB = firebase.FirebaseApplication('https://console.firebase.google.com/u/0/project/accountable-tech/database/accountable-tech-default-rtdb/data/~2F', None)

print(myDB)

name = 'John Doe'

data = {
    'Name': name,
    'Age': 25,
}


myDB.post('/users', data)