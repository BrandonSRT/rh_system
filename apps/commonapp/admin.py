from django.contrib import admin

from apps.commonapp.models import Candidate, Country, Jobs

# Register your models here.
class Candidate_Admin(admin.ModelAdmin):
    list_display = ("name", "gender", "name", "identification", "nationality",
                    "direction", "birth_date", "candidate_phone", "mail")

class Country_Admin(admin.ModelAdmin):
    list_display = ("id","country_name")


class Jobs_Admin(admin.ModelAdmin):
    list_display = ("id","job_name")



admin.site.register(Candidate, Candidate_Admin)
admin.site.register(Country, Country_Admin)
admin.site.register(Jobs, Jobs_Admin)
