from django.http import HttpResponse
from django.shortcuts import render
from db.models import Examples
from django.http import HttpResponseRedirect

def home(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"admin.html")

def insert(request):
    oname = (request.POST["oname"])
    oemail = (request.POST["oemail"])
    ophone = (request.POST["ophone"])
    ocity = (request.POST["ocity"])
    res = Examples(oname = oname, oemail = oemail, ophone = ophone, ocity = ocity)
    res.save()
    return HttpResponseRedirect('/account/')

def account(request):
    showdata = Examples.objects.all()
    display={'showdata' : showdata}
    return render(request,"signup.html",display)

def myprofile(request,oname):
    showdata = Examples.objects.get(oname=oname)
    dd={'showdata' : showdata}
    return render(request,"admin.html",dd)

def update(request):
    oname = (request.GET["oname"])  
    odata = Examples.objects.get(oname = oname)
    odata.oemail = (request.GET["oemail"])
    odata.ophone = (request.GET["ophone"])
    odata.ocity = (request.GET["ocity"])
    odata.save()
    return HttpResponseRedirect('/account/')
def delete(request,oname):
    odata = Examples.objects.get(oname=oname)
    odata.delete()
    return HttpResponseRedirect('/show/')