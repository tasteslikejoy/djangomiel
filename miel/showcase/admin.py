from django.contrib import admin
from .models import CandidateCard, PersonalInfo, Status, Experience, Quota, Office, Course, Skill, Invitations


# Register your models here.

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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

# @admin.register(PersonalInfo)
# class PersonalInfoAdmin(admin.ModelAdmin):
#     list_display = [
#         'id', 'last_name', 'first_name',
#         'middle_name', 'email', 'phone',
#         'city', 'date_of_birth'
#     ]
#     list_display_links = ['last_name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'workplace',
        'occupation',
        'date_start',
        'date_end',
    )


# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ['workplace', 'occupation', 'date_start', 'date_end']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = ['name']
    list_display_links = ['name']


# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     list_display_links = ['name']
#     list_filter = ['id']
#     search_fields = ['name']


# @admin.register(CandidateCard)
# class CandidateCardAdmin(admin.ModelAdmin):
#     # def invitations(self, obj):
#     #     return 0
#
#     def get_course(self, obj):
#         return ", ".join([course.name for course in obj.course.all()])
#
#     def get_skills(self, obj):
#         return ", ".join([skill.name for skill in obj.skills.all()])
#
#     get_course.short_description = 'Courses'
#     get_skills.short_description = 'Skills'
#     list_display = (
#         'id',
#         'personal_info__first_name',
#         'personal_info__last_name',
#         'personal_info__email',
#         'created_at',
#         'invitations',  #
#         'current_workplace',
#         'current_occupation',
#         'employment_date',
#         'get_course',
#         'get_skills',
#         'synopsis',
#         'experience',
#     )
#
#     search_fields = (
#         'created_at',
#         'personal_info__first_name',
#         'personal_info__last_name',
#         'personal_info__email',
#     )
#     list_filter = ('favorite', 'archived', 'invitation_to_office')


@admin.register(CandidateCard)
class CandidateCardAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'personal_info', 'employment_date',
        'favorite', 'archived', 'created_at',
    ]
    list_filter = ['id', 'created_at']
    search_fields = ['personal_info']
    list_display_links = ['personal_info']
    list_editable = ['favorite', 'archived']


@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ['office', 'quantity', 'default', 'used', 'need', 'date']
    list_editable = ['default', 'used', 'need', 'quantity']
    list_display_links = ['office']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'superviser', 'get_quota_quantity', 'get_quota_need']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']

    def get_quota_quantity(self, obj):
        if obj.quotas.all().exists():
            quota = obj.quotas.all().last()
            return quota.quantity
        else:
            return None

    get_quota_quantity.short_description = 'Квота на текущий месяц'

    def get_quota_need(self, obj):
        if obj.quotas.all().exists():
            quota = obj.quotas.all().last()
            return quota.need
        else:
            return None

    get_quota_need.short_description = 'Потребность по квоте'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']


@admin.register(Invitations)
class InvitationsAdmin(admin.ModelAdmin):
    list_display = ['office', 'status']
