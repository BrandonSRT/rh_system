from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from apps.commonapp.models import Candidate, HR_Form, Jobs




class register_user(View):
    def get(self, request):

        return render(request, "admin/register_user.html")

    def post(self, request):
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        mail = request.POST.get('email')
        password = request.POST.get('password')

        user= User.objects.create(first_name=name, last_name=lastname,username=username,email=mail)
        user.set_password(password)
        group = Group.objects.get(name='admin')
        user.groups.add(group)
        user.save()
        return render(request, "admin/register_user.html")


class search(View):
    def get(self, request):
        context={}
        query = ""
        print(request.GET.get('job'))
        jobs = Jobs.objects.all()
        if (request.GET.get('q') == "" or request.GET.get('q') == None) and (request.GET.get('job') == "" or request.GET.get('job') == None):
            print("1")
            result = Candidate.objects.all()
            paginator_candidate = Paginator(result, 10)
            page_number = request.GET.get('page')
            candidate_page_obj = paginator_candidate.get_page(page_number)
        elif request.GET.get('job') == "":
            print("2")
            query = request.GET['q']
            context['query']=str(query)
            result = get_result(query)
            context['candidates'] = result
            paginator_candidate = Paginator(result, 10)
            page_number = request.GET.get('page')
            candidate_page_obj = paginator_candidate.get_page(page_number)
        else:
            query = request.GET['job']
            context['query']=query
            result = get_job(query)
            context['candidates'] = result
            paginator_candidate = Paginator(result, 10)
            page_number = request.GET.get('page')
            candidate_page_obj = paginator_candidate.get_page(page_number)
            


        context={'candidates':candidate_page_obj,'candidate_page_obj':candidate_page_obj,"jobs":jobs}

        return render(request, "admin/search.html", context)

    # def post(self, request):
    #     context = {}
    #     query = request.POST.get('q')
    #     context['query']=str(query)

    #     result = get_result(query)
    #     context['candidates'] = result
    #     paginator_candidate = Paginator(result, 10)
    #     page_number = request.GET.get('page')
    #     candidate_page_obj = paginator_candidate.get_page(page_number)

    #     context={'candidates':candidate_page_obj,'candidate_page_obj':candidate_page_obj}
    #     return render(request, "admin/main.html", context)


class form_attached(View):
    def get(self, request, *args, **kwargs):

        hr_form_id = kwargs['pk']
        hr_form = HR_Form.objects.get(ref_num=hr_form_id)
        context = {"hr_form":hr_form}


        return render(request, "admin/form_attached.html", context)

    def post(self, request, *args, **kwargs):
        hr_form_id = kwargs['pk']
        hr_form = HR_Form.objects.get(ref_num=hr_form_id)
        hr_form.interviewed = request.POST.get("interviewed")
        hr_form.result1 = request.POST.get("result1")
        hr_form.observaciones1 = request.POST.get("observaciones1")
        hr_form.terapy = request.POST.get("terapy")
        hr_form.result2 = request.POST.get("result2")
        hr_form.observaciones2 = request.POST.get("observaciones2")
        hr_form.medicalval = request.POST.get("medicalval")
        hr_form.result3 = request.POST.get("result3")
        hr_form.observaciones3 = request.POST.get("observaciones3")
        hr_form.psychometric = request.POST.get("psychometric")
        hr_form.result4 = request.POST.get("result4")
        hr_form.observaciones4 = request.POST["observaciones4"]
        hr_form.interview_date = request.POST["interview_date"]
        hr_form.interviewers = request.POST["interviewers"]
        if(request.FILES.get('test_file') != None):
            hr_form.test_file = request.FILES.get('test_file')
        hr_form.save()


        
        return redirect("search")




def get_result(query=None):
    print(query)
    queryset = []
    queries = query.split(" ")
    for q in queries:
        if q.isnumeric():
            candidates = Candidate.objects.filter(Q(identification__icontains=q)).distinct()

        else:
            candidates = Candidate.objects.filter(Q(name__icontains=q)).distinct()

    for candidate in candidates:
        queryset.append(candidate)

    return list(set(queryset))


def get_job(query=None):
    print(query)
    queryset = []
    queries = query.split(" ")
    for q in queries:
        candidates = Candidate.objects.filter(Q(job=q)).distinct()


    for candidate in candidates:
        queryset.append(candidate)

    return list(set(queryset))


