from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() # забираем кастомную модель


class Quota(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    default = models.IntegerField(null=True, blank=True)
    used = models.IntegerField(null=True, blank=True)
    need = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)


class Office(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link_to_admin = models.CharField(max_length=255, null=True, blank=True) # tastes_like_joy + t.me/

    superviser = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    quota = models.ForeignKey(Quota, null=True, blank=True, on_delete=models.CASCADE)


class Status(models.Model):
    name = models.CharField(max_length=255)


class Experience(models.Model):
    workplace = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)


class PersonalInfo(models.Model):

    class Genders(models.TextChoices):
        male = 'male', 'мужской'
        female = 'female', 'женский'

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    contact_link = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(choices=Genders, max_length=6, null=True, blank=True)
    date_of_birth = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=50)


class Skill(models.Model):
    name = models.CharField(max_length=50)


class CandidateCard(models.Model):
    created_at = models.DateField(auto_now_add=True)
    current_workplace = models.CharField(max_length=255, null=True, blank=True) # где сейчас
    current_occupation = models.CharField(max_length=255, null=True, blank=True) # кем сейчас
    employment_date = models.DateField(null=True, blank=True) # дата трудоустройства (авто по статусу)
    comment = models.CharField(max_length=300)
    favorite = models.BooleanField(default=False, blank=True)
    archived = models.BooleanField(default=False, blank=True)
    synopsis = models.CharField(max_length=255, null=True, blank=True) # ссылка на резюме

    objects_card = models.IntegerField(verbose_name='Объекты', null=True, blank=True)
    clients_card = models.IntegerField(verbose_name='Клиенты', null=True, blank=True)

    invitation_to_office = models.ForeignKey('Invitations', null=True, blank=True, on_delete=models.SET_NULL)
    experience = models.ForeignKey(Experience, null=True, blank=True, on_delete=models.SET_NULL)
    personal_info = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)

    course = models.ManyToManyField('CandidateCourse')
    skills = models.ManyToManyField('CandidateSkill')


class Invitations(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class CandidateCourse(models.Model):
    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0, blank=True)


class CandidateSkill(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)
