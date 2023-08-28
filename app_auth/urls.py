from django.shortcuts import render

# Create your views here.
def advertisment_post(request):
    return render(request,"advertisement-post.html")