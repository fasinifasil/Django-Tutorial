from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect


from SchoolUserApp.models import RegisterData


# Create your views here.
def LoadHomepage(request):
    return render(request,'Homepage.html')
def LoadGallerypage(request):
    return render(request,'GalleryPage.html')
#
# def RegisterPage(request):
#         if request.method == 'POST':
#             registerdata = RegisterForm(request.POST)
#             if registerdata.is_valid():
#                 registerdata.save()
#                 return redirect('login')
#         Registerform = RegisterForm()
#         dict_form = {
#             'register': Registerform
#         }
#         return render(request,'RegisterPage.html',dict_form)
#
#
# views.py
from django.shortcuts import render, redirect
from .forms import RegisterDataForm

def RegisterPage(request):
    if request.method == 'POST':
        form = RegisterDataForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user data to the database
            # Redirect to a success page or another appropriate page
            return HttpResponse('success-Student-name')
    else:
        form = RegisterDataForm()

    return render(request, 'registration/register.html', {'form': form})
