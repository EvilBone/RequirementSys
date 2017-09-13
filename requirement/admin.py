from django.contrib import admin
from .models import Requirement
# Register your models here.
class RequirementAdmin(admin.ModelAdmin):
    fields = ('req_summary','req_des','req_raise_date','req_raise_user','req_raise_dep','req_priority','req_expect_date','req_doc_finish_date','req_status','req_developer','req_doc_link')
    list_display = ('id','req_summary','req_des','req_raise_date','req_raise_user','req_raise_dep','req_priority','req_expect_date','req_doc_finish_date','req_status','req_developer','req_doc_link')

admin.site.register(Requirement,RequirementAdmin)