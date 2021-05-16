from django import forms
import datetime

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question text')
    pub_date = forms.DateField(
        widget=forms.SelectDateWidget,
        initial=datetime.datetime.now(),
        label='Published Date'
        )
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
        )