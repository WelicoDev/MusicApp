from django.db import models
from shared.models import BaseModel
from django.core.validators import FileExtensionValidator, MaxLengthValidator

# Create your models here.
class Artist(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='artist/', validators=[
        FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png' , 'svg' , 'webp'])])
    bio = models.TextField(validators=[MaxLengthValidator(2500)])

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Music(BaseModel):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='music/', validators=[
        FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'svg', 'webp'])])
    audio_file = models.FileField(upload_to='music', validators=[
        FileExtensionValidator(allowed_extensions=['mp3', 'ogg', 'wav', 'aac', 'mp4'])
    ])
    audio_link = models.CharField(max_length=255, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str(self):
        return f"{self.title} -- > {self.author.full_name}"

