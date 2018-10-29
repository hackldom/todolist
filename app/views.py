from flask import render_template, request
from app import app
#from .forms import PostData
from form import AddNoteForm


app.secret_key = 'Development Key'

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
                           
@app.route('/submitted', methods=['GET','POST'])
def addToDo():
        user = {'name': 'Dom Hackl'}
        tabs = ["Add Element", "View All Entries", "View Uncompleted Entries", "View Completed Entries"]
        #form = PostData()
        #if form.validate_on_submit():
         #       flash('Successfully received form data. The title is %s and the description is %s = %s'%(form.title.data, form.desc.data))
        #if request.method == 'POST':
         #       title = request.form['noteTitle']
          #      desc = request.form['noteDetail']
        form = AddNoteForm()
        if request.method == 'POST':
                return "success"
        elif request.method == 'GET':
                return render_template('submitted.html',
                        user=user,
                        tabs=tabs,
                        title='Add a New Note',
                        form=form)

       

