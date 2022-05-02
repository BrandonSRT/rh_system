from traceback import print_tb
from django.shortcuts import redirect, render
from django.views import View
from datetime import datetime
from django.contrib import messages

from apps.commonapp.models import Candidate, Country, HR_Form, Jobs

# Create your views here.


class candidateForm(View):
    def get(self, request):
        fecha = datetime.now()
        today = fecha.strftime('%Y-%m-%d')
        nationalities = Country.objects.all()   
        jobs = Jobs.objects.all()

        context = {"nationalities": nationalities,"jobs":jobs, "today":today}
        return render(request, "user/CandidateForm.html",context)

    def post(self, request):
        jobs = Jobs.objects.all()
        nationalities = Country.objects.all()
        name = request.POST.get('Name')
        gender = request.POST.get('GenderOption')
        identification = request.POST.get('identification')
        nationality = Country.objects.get(pk=request.POST['Nationality'])
        direction = request.POST.get('Direction')
        birth_date = request.POST.get('birthday')
        candidate_phone = request.POST.get('Phone')
        mail = request.POST.get('email')
        civil_status = request.POST.get('civil_status')
        spouse = request.POST.get('spouse')
        children_option = request.POST.get('childrenOption')
        children_quantity = request.POST.get('quantity')
        dependency_quantity = request.POST.get('peopledependecy')
        blood_type = request.POST.get('bloodtype')
        license_type = request.POST.get('license')
        vehicle_option = request.POST.get('vehicleOption')
        profession = request.POST.get('profession')
        job = Jobs.objects.get(pk=request.POST['job'])
        salary = request.POST.get('salarypretension')
        date = request.POST.get('date')
        studies = request.POST.get('studies')
        illness_option = request.POST.get('illnessOption')
        illness = request.POST.get('illness')
        company_name = request.POST.get('companyname')
        compnay_phone = request.POST.get('phone2')
        old_job = request.POST.get('job2')
        final_salary = request.POST.get('finalsalary')
        entry_date = request.POST.get('entrydate')
        departure_date = request.POST.get('departuredate')
        boss_name = request.POST.get('bossname')
        exit_reason = request.POST.get('reason')
        family_option = request.POST.get('familyOption')
        familiar = request.POST.get('who')
        other_studies = request.POST.get('studies_other')
        handling = request.POST.get('handling')
        cv = request.FILES.get('cv')
        photo = request.FILES.get('File')
        profesional_code= request.POST.get('profesional_code')
        person_name1 = request.POST.get('person_name1')
        person_phone1 = request.POST.get('person_phone1')
        person_name2 = request.POST.get('person_name2')
        person_phone2 = request.POST.get('person_phone2')
        vehicle_description = request.POST.get('vehicle_description')
        hogar_employee = request.POST.get('hogar_employee')


        candidate = Candidate.objects.create(name=name,gender=gender,identification=identification,nationality=nationality,
        direction=direction,birth_date=birth_date,candidate_phone=candidate_phone,mail=mail,civil_status=civil_status,
        spouse=spouse,children_option=children_option,children_quantity=children_quantity,dependency_quantity=dependency_quantity,
        blood_type=blood_type,license_type=license_type,vehicle_option=vehicle_option,profession=profession,job=job,
        salary=salary,date=date,studies=studies,illness_option=illness_option,illness=illness,company_name=company_name,
        compnay_phone=compnay_phone,old_job=old_job,final_salary=final_salary,entry_date=entry_date,departure_date=departure_date,
        boss_name=boss_name,exit_reason=exit_reason,family_option=family_option,familiar=familiar,photo=photo, cv=cv,handling_option=handling,
        other_studies=other_studies,profesional_code=profesional_code,person_name1=person_name1,person_phone1=person_phone1,person_name2=person_name2,
        person_phone2=person_phone2,vehicle_description=vehicle_description,hogar_employee=hogar_employee)
        candidate.save()

        hr_form = HR_Form.objects.create(ref_num=candidate.id,name=candidate.name,interviewed=False,result1=False,terapy=False,result2=False,medicalval=False,result3=False,psychometric=False,interview_date=date)
        hr_form.save()

        context = {"nationalities": nationalities,"jobs":jobs}
        messages.success(request, "!Se ha registrado su información con éxito¡")

        return render(request, "user/CandidateForm.html",context)


class candidateFormedit(View):
    def get(self, request, *args, **kwargs):
        nationalities = Country.objects.all()
        jobs = Jobs.objects.all()
        candidateid = kwargs['pk']
        candidate = Candidate.objects.get(pk=candidateid)
        context = {"nationalities": nationalities,"jobs":jobs ,"candidate":candidate, "candidateid":candidateid}
        return render(request, "user/CandidateFormedit.html",context)

    def post(self, request, *args, **kwargs):
        nationalities = Country.objects.all()
        jobs = Jobs.objects.all()
        candidateid = kwargs['pk']
        candidate = Candidate.objects.get(pk=candidateid)
        candidate.name = request.POST.get('Name')
        candidate.gender = request.POST.get('GenderOption')
        candidate.identification = request.POST.get('identification')
        candidate.nationality = Country.objects.get(pk=request.POST['Nationality'])
        candidate.direction = request.POST.get('Direction')
        candidate.birth_date = request.POST.get('birthday')
        candidate.candidate_phone = request.POST.get('Phone')
        candidate.mail = request.POST.get('email')
        candidate.civil_status = request.POST.get('civil_status')
        candidate.spouse = request.POST.get('spouse')
        candidate.children_option = request.POST.get('childrenOption')
        candidate.children_quantity = request.POST.get('quantity')
        candidate.dependency_quantity = request.POST.get('peopledependecy')
        candidate.blood_type = request.POST.get('bloodtype')
        candidate.license_type = request.POST.get('license')
        candidate.vehicle_option = request.POST.get('vehicleOption')
        candidate.profession = request.POST.get('profession')
        candidate.job = Jobs.objects.get(pk=request.POST['job'])
        candidate.salary = request.POST.get('salarypretension')
        candidate.date = request.POST.get('date')
        candidate.studies = request.POST.get('studies')
        candidate.illness_option = request.POST.get('illnessOption')
        candidate.illness = request.POST.get('illness')
        candidate.company_name = request.POST.get('companyname')
        candidate.compnay_phone = request.POST.get('phone2')
        candidate.old_job = request.POST.get('job2')
        candidate.final_salary = request.POST.get('finalsalary')
        candidate.entry_date = request.POST.get('entrydate')
        candidate.departure_date = request.POST.get('departuredate')
        candidate.boss_name = request.POST.get('bossname')
        candidate.exit_reason = request.POST.get('reason')
        candidate.family_option = request.POST.get('familyOption')
        candidate.familiar = request.POST.get('who')
        candidate.other_studies = request.POST.get('studies_other')
        candidate.handling = request.POST.get('handling')
        if(request.FILES.get('cv') != None):
            candidate.cv = request.FILES.get('cv')
        if(request.FILES.get('File') != None):
            candidate.photo = request.FILES.get('File')
        candidate.profesional_code= request.POST.get('profesional_code')
        candidate.person_name1 = request.POST.get('person_name1')
        candidate.person_phone1 = request.POST.get('person_phone1')
        candidate.person_name2 = request.POST.get('person_name2')
        candidate.person_phone2 = request.POST.get('person_phone2')
        candidate.vehicle_description = request.POST.get('vehicle_description')
        candidate.hogar_employee = request.POST.get('hogar_employee')


        candidate.save()
        context = {"nationalities": nationalities,"jobs":jobs ,"candidate":candidate, "candidateid":candidateid}


        return render(request, "user/CandidateFormedit.html",context)


def candidate_delete (request, id):

    if request.method == 'POST':
        try:
            candidate = Candidate.objects.get(pk=id)
            candidate.delete()
            return redirect('search')
        except:
            return redirect('search')

    return render(request, 'user/delete_candidate.html')