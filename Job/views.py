from django.shortcuts import redirect, render

# Created By Me
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    # print(job_list)


    # filters
    myfilter = JobFilter(request.GET ,queryset=job_list)
    job_list = myfilter.qs # job_list after filtering

    # pagination
    paginator = Paginator(job_list, 3) # Show # of jobs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj ,'myfilter':myfilter} # template name
    return render(request , 'job/job_list.html' ,context)


def job_detail(request , slug):
    job_detail = Job.objects.get(slug = slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    
    context = {'job' : job_detail , 'form':form}
    return render(request , 'job/job_detail.html' ,context)

@login_required
def add_job(request):
    # save data from the form
    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()

            # show new job in job list
            return redirect(reverse('jobs:job_list'))
    # show the form
    else:
        form = JobForm()

    return render(request , 'job/add_job.html' , {'form':form})