from flask import render_template
from app import app

@app.route('/')
def index():
    user = {'name': 'Dom Hackl',
            'age': 20,
            'nationality': 'Hungarian'}

    menu = ["Add Element", "View All Entries", "View Uncompleted Entries", "View Completed Entries"]

          

    return render_template('index.html',
                            title='Simple template example',
                            user=user,
                            menu=menu)


    
@app.route('/friends')    
def people():
    people = ["Adam", "Kieran", "John", "Mike"]
    return render_template('people.html',
                            people=people)