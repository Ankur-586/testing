from django.contrib.auth.models import User
from .models import Subject, combined
import django_filters
# pip install django-filter  

class UserFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(lookup_expr='icontains')
    # last_name = django_filters.CharFilter(lookup_expr='icontains')
    # datejoined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    class Meta:
        model = User
        fields = ['first_name','last_name']

class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = ['Subject_name']

class combineFilter(django_filters.FilterSet):
    class Meta:
        model = combined
        fields = ['subject','student']