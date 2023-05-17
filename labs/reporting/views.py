from django.shortcuts import render,redirect

def dashboard(request):
    context = {}
    template_name = "dashboard.html"
    return render (request, template_name,context)
