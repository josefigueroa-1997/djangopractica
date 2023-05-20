from django.shortcuts import render,redirect
from .models import Report



def dashboard(request):
    report = Report.objects.all()
    context = {'report': report}
    template_name = "dashboard.html"
    return render (request, template_name,context)


def formreport(request):
    rep = Report()
    template_name= "formreport.html"
    if request.method == 'POST':
        rep.descripcion = request.POST['descripcion']
        rep.save()
        return redirect ('dashboard')
    context = {}
    return render (request,template_name,context)