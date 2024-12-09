from django.contrib import admin
from .models import CandidateCard, PersonalInfo, Status, Experience

# Register your models here.


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'contact_link',
        'first_name',
        'last_name',
        'middle_name',
        'city',
        'gender',
        'date_of_birth',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'workplace',
        'occupation',
        'date_start',
        'date_end',
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(CandidateCard)
class CandidateCardAdmin(admin.ModelAdmin):
    def invitations(self, obj):
        print('*****************')
        print('*****************')
        print(type(obj))
        print('*****************')
        print('*****************')
        return 0

    def get_course(self, obj):
        return ", ".join([course.name for course in obj.course.all()])

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    get_course.short_description = 'Courses'
    get_skills.short_description = 'Skills'

    list_display = (
        'created_at',
        'current_workplace',
        'current_occupation',
        'employment_date',
        'synopsis',
        'invitations',  #
        'status',
        'experience',
        'get_course',
        'get_skills',
        'personal_info__first_name',
        'personal_info__last_name',
        'personal_info__email',
    )
    search_fields = (
        'created_at',
        'personal_info__first_name',
        'personal_info__last_name',
        'personal_info__email',
    )
    list_filter = ('favorite', 'archived', 'invitation_to_office')
