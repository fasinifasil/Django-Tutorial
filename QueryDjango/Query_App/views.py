from django.shortcuts import render

from Query_App.models import StudentData


# Create your views here.
def ShowData(request):
    data = StudentData.objects.all()
    dic1={'studentlist':data}
    return render(request,'StudentDatapage.html',dic1)
