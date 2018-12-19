from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone
from .forms import UserForm, QuestionForm
from .models import Result
from .lib import analsys

def apt_index(request):
    if request.method == 'POST':
        form = UserForm(request.POST);          
        #q_form = QuestionForm(request.POST);
        if form.is_valid():
            data_complete = True;
            answer_list = [];
            missing_list = [];

            f_name = form.cleaned_data['m_name'];
            f_sex = form.cleaned_data['m_sex'];
            f_age = form.cleaned_data['m_age'];
            f_email = form.cleaned_data["m_email"];

            #f_q1 = form.cleaned_data['q1'];
            anal = analsys.analsys("/home/pi/Project/python/django_test/django_apt_test/apttest/lib/result.json");

            #return HttpResponse(f_email);

            for i in range(1,33):
                q_index = "q" + str(i);
                #answer_list[i]["answer"] = request.POST[q_index];
                if not request.POST.get(q_index, False):
                    data_complete = False;
                    missing_list.append(q_index);
                else:
                    answer_list.append(request.POST[q_index]);

            if not data_complete:
                err_msg = ", ".join(missing_list);
                err_msg = "Oops! These following questions must be filled up, please.<br>"+err_msg;
                return HttpResponse(err_msg);

            f_type = anal.aptAlgo(answer_list);
            f_result_list = anal.getFinalResult(f_type);
            #anal.getCountResult(); #for debug using

            m_result = Result(name=f_name, sex=f_sex, age=f_age, email=f_email, answer=answer_list, person_type=f_type);
            m_result.submit();
            #return HttpResponse(f_type);
            return render(request, 'apttest/apt_result.html', {'left_l': f_result_list[0:2], 'right_l': f_result_list[2:4], 'top_l': f_result_list[4:6], 'bottom_l': f_result_list[6:8], 'main_l': f_result_list[8:10] });
     
    else:
        form = UserForm();
        q_form = QuestionForm();
        #results = Result.objects.filter(submitted_date__lte=timezone.now()).order_by('submitted_date')

        #return render(request, 'apttest/apt_index.html', {'user_form': form});
        return render(request, 'apttest/apt_index.html', {'user_form': form, 'question_form': q_form});
