from .models import *

# custom functions made by me


def authenticate(username, password, temp) :
    for i in temp:
        if i['username'] == username :
            if i['password'] == password:
                return True, True
            else : 
                return True, False
    return False , False


def get_data():
    leads = Lead.objects.all()
    data = []
    for i in leads:
        sender_opco : Employee.objects.get(name = i.submitted_by).opco
        if Employee.objects.filter(name = i.submitted_by).exists() :
            sender_opco = Employee.objects.get(name = i.submitted_by).OpCo
        else :
            sender_opco = "UNKNOWN"
        if Employee.objects.filter(name = i.submitted_to).exists() :
            receiver_opco = Employee.objects.get(name = i.submitted_to).OpCo
        else :
            receiver_opco = "UNKNOWN"
        data.append({'submitted_by' : i.submitted_by , 'submitted_to' : i.submitted_to , 'date' : clean_date(i.date_created), 'id' : i.leadid, 'sender_opco': sender_opco , 'receiver_opco' : receiver_opco})
    return data


def clean_date(date):
    new_date = date.strftime('%d') + '/' + date.strftime('%m') + '/' + date.strftime('%y') + "    " + date.strftime('%H') + ':' + date.strftime('%M') + ':' + date.strftime('%S')
    return new_date

