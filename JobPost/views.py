from django.shortcuts import render

from .forms import JobPostForm

# Create your views here.

def job_post_create_view(request):
    form = JobPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = JobPostForm()

    context = {
        'form' : form
    }

    return render(request, "JobPost/create.html", context)