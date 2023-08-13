from django import forms
import datetime

class AsteroidRequestForm(forms.Form):
    date_start = forms.DateTimeField(label='Start date', initial=datetime.datetime.today())
    date_end = forms.DateTimeField(label='End date', required=False)
    objects_count = forms.IntegerField(label='Count of objects')
