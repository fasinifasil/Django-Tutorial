from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RegisterForm

def LoadHomepage(request):
    return render(request,'Homepage.html')
def LoadGallerypage(request):
    return render(request,'GalleryPage.html')
#
def StudentDashboard(request):
    return render(request,'student_dashboard.html')
def StaffDashboard(request):
    return render(request,'staff_dashboard.html')
def AdminDashboard(request):
    return render(request,'admin_dashboard.html')
def EditorDashboard(request):
    return render(request,'editor_dashboard.html')
def register_student(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'a'
            user.save()
            return redirect('login')

    form = RegisterForm()
    return render(request, 'student_registration.html', {'form': form})

def register_staff(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'b'  # 'b' represents 'staff'
            user.save()
            return redirect('login')  # Redirect to the staff dashboard or a suitable page

    form = RegisterForm()
    return render(request, 'staff_registration.html', {'form': form})

def register_admin(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'c'
            user.save()
            return redirect('login')

    form = RegisterForm()
    return render(request, 'admin_registration.html', {'form': form})

def register_editor(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'd'
            user.save()
            return redirect('login')

    form = RegisterForm()
    return render(request, 'editor_registration.html', {'form': form})


from django.contrib import messages, auth


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = authenticate(request, username=username, password=password, role=role)

        if user is not None:
            login(request, user)
            if user.role == "a":
                return redirect('student-dashboard')
            elif user.role == "b":
                return redirect('staff-dashboard')
            elif user.role == "c":
                return redirect('admin-dashboard')
            elif user.role == "d":
                return redirect('editor-dashboard')
        else:
            messages.error(request, "Invalid login credentials.")

    return render(request, 'LoginPage.html')



def logout(request):
    auth.logout(request)
    return redirect('/')