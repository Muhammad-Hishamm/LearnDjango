from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectList=[
    {
        'id':"1",
        'title':"The first Id",
        'description':"the Describtion of the first"
    }
    ,
    {
        'id':"2",
        'title':"The second Id",
        'description':"the Describtion of the second"
    }
    ,
    {
        'id':"3",
        'title':"The third Id",
        'description':"the Describtion of the third"
    }
    
]

def projects(request):
    return render(request,'projects/projects.html',{'list':projectList})



def project(request,pk):
    projectObj=None 
    for i in projectList:
        if i['id'] == pk:
            projectObj=i          
    return render(request,'projects/single-project.html',{'i':projectObj})