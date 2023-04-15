# notes
A simple note taking app made with python and sql 

## getting started
I'm a writer and former journalist. Note-taking has been a huge part of my professonal and personal life for as long as I can remember. This was my first experience using Python, SQL, and Peewee. 

## basic components 
I wanted this app to have some of the elements I find helpful with note-taking. Before I got started, I pseudo coded some of the features I wanted which included: `add one`, `view_all`, and `search`. I'm really most proud of the app's search feature. 

### more on search
The search feature was a stretch goal. It was something I have tried to build out in other apps and haven't been able to make work. This one, however, works well. I think this is because of the SQL database. Below is the code I used. You can see the function executes a keyword search on both body and title. 

```
def search_notes(): 
    query = input('Search notes > ')
    notes = Note.select().where((Note.title.contains(query)) | (Note.body.contains(query)))
    if not notes: 
        print(f'Nothing found for {query}')
    else: 
        for i, note in enumerate(notes): 
            print(f'{i+1} {note.created_at} {note.title}: {note.body}')
```
### about the while loop
Finally, I choose to use a while loop. The loop will run until the user enters "4" and exits the program. This works well. It's nice to have a way of running this app that doesn't require the user to restart each time they want to make a change. 

## next steps
A couple more feature I would like to add. 
* First, add delete feature
* Second, build out user interface. 