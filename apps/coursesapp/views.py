from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    print "hello i am the index page return statement"
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    #add this user to the db
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def confirmdel(request, id):
    banana = Course.objects.get(id = id)
    context = {
        "course": banana
    }
    return render(request, 'coursesapp/confirm.html', context)

def delete(request, id):
    #actually delete from db after confirmation
    blah = Course.objects.get(id = id)
    blah.delete()
    #get this, put it in a variable, then delete the variable. why does this work?
    #this is based on id as a variable <id> and then delete based on id.
    #query = "delete from table where id = <id>""
    return redirect('/')




#create database
#make appropriate references to it from this code.
#dont forget to migrate.
