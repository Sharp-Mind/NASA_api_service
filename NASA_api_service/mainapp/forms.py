from django import forms
import datetime

offset = datetime.timedelta(hours=3)
tz = datetime.timezone(offset, name='')
dt = datetime.datetime.now()
tz.utcoffset(dt)

class AsteroidRequestForm(forms.Form):
    start_date = forms.DateField(label='Start date', initial='YYYY-MM-DD')
    end_date = forms.DateField(label='End date', required=False)
    objects_count = forms.IntegerField(label='Count of objects')
