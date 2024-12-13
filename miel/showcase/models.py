from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() # забираем кастомную модель


class Quota(models.Model):
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Квота на текущий месяц')
    default = models.IntegerField(null=True, blank=True, verbose_name='Квота по дефолту')
    used = models.IntegerField(null=True, blank=True, verbose_name='Использованная квота')
    need = models.IntegerField(null=True, blank=True, verbose_name='Потребность по квоте')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name='Квоту'
        verbose_name_plural = 'Квоты'

    def __str__(self):
        return f'{self.quantity}'


class Office(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название офиса')
    location = models.CharField(max_length=255, verbose_name='Адрес')
    link_to_admin = models.CharField(max_length=255, null=True, blank=True, verbose_name='Связь с админом')  # tastes_like_joy + t.me/

    superviser = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='ФИО руководителя')
    quota = models.ForeignKey(Quota, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Квота на текущий месяц')

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Experience(models.Model):
    workplace = models.CharField(max_length=255, null=True, blank=True, verbose_name='Предыдущий опыт')
    occupation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')
    date_start = models.DateField(null=True, blank=True, verbose_name='Начало работы')
    date_end = models.DateField(null=True, blank=True, verbose_name='Окончание работы')

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'

    def __str__(self):
        return self.workplace


class PersonalInfo(models.Model):

    class Genders(models.TextChoices):
        male = 'male', 'мужской'
        female = 'female', 'женский'

    email = models.EmailField(null=True, blank=True, verbose_name='Почта')  # TODO обсудить уникальность поля
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
    contact_link = models.CharField(max_length=255, null=True, blank=True, verbose_name='Связь с кандидатом')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    city = models.CharField(max_length=50, verbose_name='Город')
    gender = models.CharField(choices=Genders, max_length=6, null=True, blank=True, verbose_name='Пол')
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Персональную информацию'
        verbose_name_plural = 'Персональная информация'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class CandidateCard(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='Создана')
    current_workplace = models.CharField(max_length=255, null=True, blank=True, verbose_name='Место работы') # где сейчас
    current_occupation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность') # кем сейчас
    employment_date = models.DateField(null=True, blank=True, verbose_name='Дата трудоустройства') # дата трудоустройства (авто по статусу)
    comment = models.CharField(max_length=300, verbose_name='Комментарии')
    favorite = models.BooleanField(default=False, blank=True, verbose_name='Избранное')
    archived = models.BooleanField(default=False, blank=True, verbose_name='Архив')
    synopsis = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка на резюме') # ссылка на резюме

    objects_card = models.IntegerField(verbose_name='Объекты', null=True, blank=True)
    clients_card = models.IntegerField(verbose_name='Клиенты', null=True, blank=True)

    invitation_to_office = models.ForeignKey('Invitations', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Приглашений в офис')
    experience = models.ForeignKey(Experience, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Опыт')
    personal_info = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE, verbose_name='Персональная информация')

    course = models.ManyToManyField('CandidateCourse', blank=True, verbose_name='Курсы')
    skills = models.ManyToManyField('CandidateSkill', blank=True, verbose_name='Навыки')

    class Meta:
        verbose_name = 'Карточку кандидата'
        verbose_name_plural = 'Карточка кандидата'

    def __str__(self):
        return f'{self.personal_info.last_name} {self.personal_info.first_name} {self.personal_info.middle_name} ID: {self.id}'



class Invitations(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name='Офис')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашение'

    def __str__(self):
        return self.office.name


class CandidateCourse(models.Model):
    progress = models.IntegerField(default=0, verbose_name='Прогресс')

    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CandidateSkill(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateCard, on_delete=models.CASCADE)
