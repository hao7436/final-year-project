from django.contrib import admin
from .models import *

# Register your models here.
class StoriesAdmin(admin.ModelAdmin):
 list_display = ('authorFname', 'authorLname',
                'authorEmail', 'authorNumber', 'scamTitle', 'scamType',
                 'nameOfScamer', 'contentOfScamer', 'emailOfScamer', 'scamDetail', 'timestamp')
 
   
class CooperationAdmin(admin.ModelAdmin):
 list_display = ('organisationName', 'organisationEmail',
                'personInContact', 'ContactNumber', 'cooperationDetail', 'timestamp')

class JoinActivitesAdmin(admin.ModelAdmin):
 list_display = ('activitesTitle', 'joinerName','joinerEmail', 'joinerContactNumber',
                 'joinerDob', 'joinAs')

class AddActivitesAdmin(admin.ModelAdmin):
 list_display = ('activitesTitle', 'activitesDetail','activitesLocation', 'activitesCooperateWith',
                 'activitesDate', 'activitesTime','toDo','canJoinAs')


admin.site.register(Stories, StoriesAdmin)
admin.site.register(Cooperation, CooperationAdmin)
admin.site.register(JoinActivites, JoinActivitesAdmin)
admin.site.register(AddActivites, AddActivitesAdmin)