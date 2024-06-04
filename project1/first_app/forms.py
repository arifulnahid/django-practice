from django import forms
import datetime
from .models import App


class AppForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(widget=forms.NumberInput(
        attrs={'type': 'date'}), initial=datetime.date.today)
    dob = forms.DateField(
        widget=forms.SelectDateWidget(years=[1999, 2000, 2001]))
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[
                                      ('gree', 'Green'), ('red', 'Red')])


class AppModelForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'
