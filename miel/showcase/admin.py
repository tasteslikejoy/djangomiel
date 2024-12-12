from django.contrib import admin
from .models import *


# @admin.register(Quota)
# class QuotaAdmin(admin.ModelAdmin):
#     list_display = ['quantity', 'default', 'used', 'need', 'date']
#     list_editable = ['default', 'used', 'need', 'quantity']
#     list_display_links = ['date']

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'superviser', 'get_quota_quantity']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']

    def get_quota_quantity(self, obj):
        return obj.quota.quantity if obj.quota else None

    get_quota_quantity.short_description = 'Квота на текущий месяц'

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']

# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ['workplace', 'occupation', 'date_start', 'date_end']

# @admin.register(PersonalInfo)
# class PersonalInfoAdmin(admin.ModelAdmin):
#     list_display = [
#         'id', 'last_name', 'first_name',
#         'middle_name', 'email', 'phone',
#         'city', 'date_of_birth'
#     ]
#     list_display_links = ['last_name']

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

# @admin.register(Invitations)
# class InvitationsAdmin(admin.ModelAdmin):
#     list_display = ['office', 'status']











