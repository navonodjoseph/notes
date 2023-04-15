from peewee import * 
from datetime import datetime

db = PostgresqlDatabase(
    'notes', # name of the database 
    user = '', # name of the user
    password = '', # password 
    host = 'localhost', # name of the host
    port = 5432 # port 
)

# connect to database 
db.connect()

# create a model 

class BaseModel(Model):
    class Meta: 
        database = db

class Note(BaseModel): 
    title= CharField() #varchar
    body= TextField() #textfield
    created_at = DateField()

# create table in the database 
db.create_tables([Note]) # then, create the tables from scratch


# add a new note to database 
def add_note(): 
   title = input('Title >  ')
   body = input('Enter body of note > ')
   created_at = datetime.now()
   note = Note(title=title, body=body, created_at=created_at)
   note.save()

# add a function to show all the notes 

def show_notes(): 
    notes = Note.select().order_by(Note.created_at.desc())
    if not notes: 
        print('There are no notes.')
    else: 
        for i, note in enumerate(notes): 
            print(f'{i+1} {note.created_at} {note.title}: {note.body}')

# create search function 
def search_notes(): 
    query = input('Search notes > ')
    notes = Note.select().where((Note.title.contains(query)) | (Note.body.contains(query)))
    if not notes: 
        print(f'Nothing found for {query}')
    else: 
        for i, note in enumerate(notes): 
            print(f'{i+1} {note.created_at} {note.title}: {note.body}') 

# PART II
# create condtionals and menu 
while True: 
  print("""       
  
               NOTEBOOK        
""")
  print("""
  This is where you can take notes
  and find them later. All entries are 
  saved in a database and searchable
  """)
  print()
  print('What would you like to do?')
  print()
  print('1.  Add new')
  print('2.  Show all')
  print('3.  Search')
  print('4.  Exit')
  print()
  choice = input('Enter your choice (1-4): ')
  if choice == '1': 
      add_note()
  elif choice =='2': 
      show_notes()
  elif choice =='3': 
      search_notes()
  elif choice =='4': 
      break
  else: 
      print("Invalid entry. Please enter 1 - 4")