from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() # забираем кастомную модель


class Office(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link_to_admin = models.CharField(max_length=255, null=True, blank=True) # tastes_like_joy + t.me/

    superviser = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)


class Quota(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    default_quota = models.IntegerField(null=True, blank=True)
    user_quota = models.IntegerField(null=True, blank=True)
    need_quota = models.IntegerField(null=True, blank=True)

    office = models.OneToOneField(Office, null=True, blank=True, on_delete=models.CASCADE)


class Status(models.Model):
    name = models.CharField(max_length=255)


class Experience(models.Model):
    workplace = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)


class PersonalInfo(models.Model):

    class Genders(models.TextChoices):
        male = 'ma', 'мужской'
        female = 'fe', 'женский'

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    contact_link = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(choices=Genders, max_length=2, null=True, blank=True)
    date_of_birth = models.DateTimeField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    progress = models.IntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=50)


class CandidateCard(User):
    created_at = models.DateTimeField(auto_now_add=True)
    current_workplace = models.CharField(max_length=255, null=True, blank=True) # где сейчас
    current_occupation = models.CharField(max_length=255, null=True, blank=True) # кем сейчас
    employment_date = models.DateTimeField(null=True, blank=True) # дата трудоустройства (авто по статусу)
    comment = models.CharField(max_length=300)
    favorite = models.BooleanField(default=False, blank=True)
    archived = models.BooleanField(default=False, blank=True)
    synopsis = models.CharField(max_length=255, null=True, blank=True) # ссылка на резюме

    objects_card = models.IntegerField(verbose_name='Объекты', null=True, blank=True)
    clients_card = models.IntegerField(verbose_name='Клиенты', null=True, blank=True)

    invitation_to_office = models.ForeignKey(Office, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.SET_NULL)  # TODO доработать статусы
    experience = models.ForeignKey(Experience, null=True, blank=True, on_delete=models.SET_NULL)
    personal_info = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)

    course = models.ManyToManyField('CandidateCourse')
    skills = models.ManyToManyField('CandidateSkill')
class CandidateCourse(models.Model):
    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CandidateSkill(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)