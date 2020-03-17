from django.db import models



# Create your models here.

# stworzenie wpisu w bazie danych
# https://www.youtube.com/watch?v=ExTaxRmDnP8
# pobieranie elemenetów z Django Admina
# https://www.youtube.com/watch?v=5jWJBpS0tkg



class Post(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Player(models.Model):
    PLAYER_CHOICES = (
        ('Adam', 'Adam'),
        ('Bartek', 'Bartek'),
        ('Paweł', 'Paweł'),
        ('Mateusz', 'Mateusz'),
     )
    name = models.CharField(max_length=100 , choices = PLAYER_CHOICES)
    def __str__(self):
        return self.name
