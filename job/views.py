from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Job

# Create your views here.

def job_list(request):
    jobs_list = Job.objects.all()
    context ={'joblist':jobs_list}
    return render(request,"job/joblist.html",context)



def job_detail(request,id):
    jobs_detail = Job.objects.get(id = id)
    context = {'detail':jobs_detail}
    return render(request,"job/jobdetail.html",context)