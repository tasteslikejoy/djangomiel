from django.contrib import admin
from django import forms

from .models import CandidateCard, PersonalInfo, Status, Experience, Quota, Office, Course, Skill, Invitations, \
    Favorites, CandidateSkill, CandidateCourse


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


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
    search_fields = ['name']
    list_display_links = ['name']


class CandidateCardAdminForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label='Статус'
    )

    class Meta:
        model = CandidateCard
        fields = '__all__'


@admin.register(CandidateCard)
class CandidateCardAdmin(admin.ModelAdmin):
    # form = CandidateCardAdminForm
    list_display = [
        'id', 'personal_info', 'employment_date',
        'archived', 'created_at'
    ]
    list_filter = ['id', 'created_at']
    search_fields = ['personal_info__name']
    list_display_links = ['personal_info']
    list_editable = ['archived']
    readonly_fields = ['get_skills', 'get_courses']

    def get_skills(self, obj):
        return ', '.join(skill.name for skill in obj.skills.all())

    get_skills.short_description = 'Навыки'

    def get_courses(self, obj):
        return ', '.join(course.name for course in obj.course.all())

    get_courses.short_description = 'Курсы'


@admin.register(CandidateSkill)
class CandidateSkillAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'skill')
    search_fields = ('candidate__personal_info__name', 'skill__name')


@admin.register(CandidateCourse)
class CandidateSkillAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'course', 'progress')
    search_fields = ('candidate__personal_info__name', 'course__name')


@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ['office', 'quantity', 'default', 'used', 'need', 'date']
    list_editable = ['default', 'used', 'need', 'quantity']
    list_display_links = ['office']


class QuotaInline(admin.TabularInline):
    model = Quota
    extra = 1
    fields = ['date', 'quantity', 'used', 'default', 'need']
    readonly_fields = ['date', 'used']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'date':
            kwargs['widget'] = admin.widgets.AdminDateWidget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def date_display(self, obj):
        return obj.date.strftime('%d, %b, %Y, %I:%M %p') if obj.date else None

    date_display.short_description = 'Дата'


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'superviser', 'get_quota_quantity',
                    'get_quota_need', 'current_quota', 'current_need']
    list_display_links = ['name']
    list_filter = ['id']
    search_fields = ['name']
    inlines = [QuotaInline]


    def get_quota_quantity(self, obj):
        quota = obj.quotas.first()
        return quota.quantity if quota else None

    get_quota_quantity.short_description = 'Квота на текущий месяц'

    def get_quota_need(self, obj):
        quota = obj.quotas.first()
        return quota.need if quota else None

    get_quota_need.short_description = 'Потребность по квоте'

    def current_quota(self, obj):
        return self.get_quota_quantity(obj)

    current_quota.short_description = 'Квота на текущий месяц'

    def current_need(self, obj):
        return self.get_quota_need(obj)

    current_need.short_description = 'Потребность по квоте'


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


@admin.register(Favorites)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['candidate_card', 'office']
