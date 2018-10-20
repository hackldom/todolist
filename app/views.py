from flask import render_template, flash
from app import app
from .forms import PostData

@app.route('/')
def index():
    user = {'name': 'Dom Hackl',
            'age': 20,
            'nationality': 'Hungarian'}

    menu = ["Add Element", "View All Entries", "View Uncompleted Entries", "View Completed Entries"]
          

    return render_template('index.html',
                            title='To do list',
                            user=user,
                            menu=menu)


    
@app.route('/friends')    
def people():
    people = ["Adam", "Kieran", "John", "Mike"]
    return render_template('people.html',
                            people=people)

                            
@app.route('/header')
def header():
        user = {'name': 'Dom Hackl',
                'age': 20,
                'nationality': 'Hungarian'}
        tabs = ["Add Element", "View All Entries", "View Uncompleted Entries", "View Completed Entries"]
        return render_template('header.html',
                                title='View Lists',
                                user=user,
                                tabs=tabs)
                           
@app.route('/addToDo', methods=['GET', 'POST'])
def addToDo():
        user = {'name': 'Dom Hackl'}
        tabs = ["Add Element", "View All Entries", "View Uncompleted Entries", "View Completed Entries"]
        form = PostData()
        if form.validate_on_submit():
                flash('Successfully received form data. The title is %s and the description is %s = %s'%(form.title.data, form.desc.data))
        return render_template('addToDo.html',
                        user=user,
                        title='Add a New Note',
                        tabs=tabs)

@app.route('/submitted', methods=['POST', 'GET'])
def submitted():
        user = {'name': 'Dom Hackl'}
        render_template('submitted.html',
                title='New Form Submitted',
                        user=user)