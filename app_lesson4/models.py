from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Advertisment(models.Model):
    title=models.CharField("заголовок",max_length=120)
    
    description= models.TextField("описание")
    price=models.DecimalField("цена", max_digits=10,decimal_places=2)
    auction=models.BooleanField("торг",help_text="отметьте,если торг возможен")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,verbose_name="Пользователь",on_delete=models.CASCADE)
    image=models.ImageField("изображение",upload_to="lesson4/")

@admin.display(description="Опубликовано")
def created_date(self):
    from django.utils import timezone
    if self.created_at.date() == timezone.now().date():
        created_at = self.created_at.time().strftime("%H:%M:%S")
        return format_html(
            '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_at
        )
    return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")


@admin.display(description="Обновлено")
def updated_date(self):
    from django.utils import timezone
    if self.updated_at.date() == timezone.now().date():
        updated_at = self.created_at.time().strftime("%H:%M:%S")
        return format_html(
            '<span style="color: limegreen; font-weight: bold;">Сегодня в {}</span>', updated_at
        )
    return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
@admin.display(description="Изображение")
def show_image(self):
        if self.image:
            return format_html(
                '<img width="50%" height="50%" src={}></img>', self.image.url
            )
def __str__(self):
    return "{}(id={id}, title={title}, price={price})".format(self.__class__.__name__, **self.__dict__)


class Meta:
    db_table = "advertisements"