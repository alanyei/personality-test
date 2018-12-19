from django import forms
from .models import Result
from .lib import question
import json

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
);
 
class UserForm(forms.Form):
    #quesions = open("/home/pi/Project/python/django_test/django_apt_test/apttest/lib/question.json");
    #questions.getQuestionDesc(1);
    #class Meta:
        #model = Result;
        #fields = ['name', 'sex', 'email', ];
    m_name = forms.CharField(max_length=20, label="姓名");
    m_sex = forms.ChoiceField(choices=SEX_CHOICES, label="性別");
    m_age = forms.DecimalField(decimal_places=0, min_value=1, max_value=99, label="年齡", help_text="A range of 1~99");
    m_email = forms.EmailField(label="E-MAIL", help_text="Please enter a valid email address.");

class QuestionForm(forms.Form):
    CHOICES = []; #Initial CHOICES array
    f_q = []; # Initial question array

    questions = question.questions("/home/pi/Project/python/django_test/django_apt_test/apttest/lib/question.json");

    CHOICES.append([('a','select 1'),
             ('b','select 2')]);
    CHOICES.append([('a','select 21'),
             ('b','select 22')]);
    for i in range(0,2):
        f_q.append(forms.ChoiceField(choices=CHOICES[i], widget=forms.RadioSelect(), label="test"));

"""
    q1 = forms.ChoiceField(choices=CHOICES[0], widget=forms.RadioSelect());
    q2 = forms.ChoiceField(choices=CHOICES[1], widget=forms.RadioSelect());
"""

