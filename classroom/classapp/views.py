from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from classapp.models import User, Classroom, Student, Teacher
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from helpers import random_str
from itertools import chain

# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('p_name') and request.POST.get('email') and request.POST.get('password'):
            u = User()
            u.username = request.POST.get('username')
            u.p_name = request.POST.get('p_name')
            u.email = request.POST.get('email')
            u.password = request.POST.get('password')
            u.save()
            messages.info(request, "You are registered successfully")
            return redirect('/login')        
    
    else:
        return render(request, "register.html")
    
def login(request):
    if request.method == 'POST':
        try:
            Userdetails = User.objects.get(username=request.POST['username'],password=request.POST['password'])
            request.session['username'] = Userdetails.username
            return redirect('/home')
        except User.DoesNotExist as e:
            messages.success(request, "Email or password is invalid...")
            
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['username']
    except:
        return render(request, 'login.html')
    return render(request, 'register.html')

def create_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        section = request.POST.get('section')
        room = request.POST.get('room')
        subject_name = request.POST.get('subject_name')
        join_code = random_str()
        current_username = request.session.get('username')
        current_user = User.objects.get(username=current_username)
        classroom = Classroom.objects.create(owner=current_user, class_name=class_name, section=section, room=room, subject_name=subject_name, join_code=join_code)
        classroom.save()
        teacher = Teacher.objects.create(username=current_user, classroom=classroom)
        teacher.save()
        return redirect('/home')
    
    else:
        return render(request, 'create_class.html')

def view_class(request):
    current_username = request.session.get('username')
    current_user = User.objects.get(username=current_username)
    s = Student.objects.filter(username=current_user)
    t = Teacher.objects.filter(username=current_user)
    classrooms = list(chain(s, t))
    return render(request, 'home.html', {
        "classrooms": classrooms
    })

def join_class(request):
    return render(request, 'join_class.html')