import django_filters

# import your models here 
from .models import *

# create your forms here 

class LeadFilter(django_filters.FilterSet) :
    class Meta :
        model = Lead
        fields = ['status']