from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import csv

# Import your forms here

from .forms import EmployeeForm, LoginForm, LeadForm
from .models import *
from .filters import *

# import your functions here

from .functions import *

# Create your views here.


def dashboard(request, user) :
    data = get_data()
    name = Employee.objects.get(name = user).name
    context = {'leads' : data, 'user' : name}
    return render(request, 'hackapp/dashboard.html', context);

def signup(request) :
    form = EmployeeForm() 
    context = {'form' : form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    return render(request, 'hackapp/signup.html', context)

def home(request):
    form = LoginForm()
    users = Employee.objects.all()
    temp = []
    context = {}
    messages = ['invalid username' , 'invalid password', 'welcome']
    for i in users :
        temp.append({'username' : i.name, 'password' : i.password})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a, b = authenticate(data['username'], data['password'], temp)
            context = {'message' : messages[a + b]}
            if(a & b) :
                return HttpResponseRedirect("/dashboard/{name}/".format(name = data['username']))
            else :
                return render(request, 'hackapp/login.html', context)
    return render(request, 'hackapp/login.html')



def newlead(request, user) :
    form = LeadForm()
    context = {'form' : form}
    if request.method == 'POST' :
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/{name}/'.format(name = user))
    return render(request, 'hackapp/newlead.html', context)



def profile(request,user):
    emp = Employee.objects.get(name = user)
    assigned = len(Lead.objects.filter(submitted_to = user, status = "OPEN"))
    submitted = len(Lead.objects.filter(submitted_by = user))
    context = {'username' : emp.name, 'email' : emp.EntEmail, 'initial' : emp.name[0].upper() , 'assigned' : assigned, 'submitted' : submitted}
    return render(request, 'hackapp/profile.html', context)

def assigned(request, user):
    leads = Lead.objects.filter(submitted_to = user)
    filter = LeadFilter(request.GET, queryset = leads)
    leads = filter.qs
    context = {'leads' : leads , 'user' : user, 'filter' : filter}
    return render(request, 'hackapp/assigned.html', context)

def submitted(request, user):
    leads = Lead.objects.filter(submitted_by = user)
    filter = LeadFilter(request.GET, queryset = leads)
    leads = filter.qs
    context = {'leads' : leads, 'user' : user, 'filter' : filter}
    return render(request, 'hackapp/submitted.html', context)


def update(request, user, status, id, origin) :
    print(user, status, id)
    if origin == "assignedpage" :
        lead = Lead.objects.get(leadid = id)
        context = {'user' : user , 'lead' : lead}
        return render(request, 'hackapp/changestatus.html', context)
    else :
        if status != "0":
            lead = Lead.objects.get(leadid = id)
            lead.status = status
            lead.save()
        return redirect('/assigned/{name}'.format(name = user))

def export(request, user) :
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['lead_id', 'lead_name', 'submitted_by', 'submitted_to', 'status', 'project', 'segment', 'date/time'])
    for lead in Lead.objects.all().values_list('leadid', 'name', 'submitted_by', 'submitted_to', 'status', 'project', 'segment', 'date_created'):
        writer.writerow(lead)
    response['Content-Disposition'] = 'attachment; filename = "leads.csv"'
    return response