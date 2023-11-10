from django.db import models


class MyUser(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


class Coord(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')


LEVEL = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
]


class Level(models.Model):
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима', null=True, blank=True, )
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето', null=True, blank=True, )
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень', null=True, blank=True, )
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна', null=True, blank=True, )


class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'New'),
        ('AC', 'Accepted'),
        ('PN', 'Pending'),
        ('RJ', 'Rejected'),
    )
    beauty_title = models.CharField(max_length=255, verbose_name='Общее название', default=None)
    title = models.CharField(max_length=255, verbose_name='Название горы', null=True, blank=True)
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название горы')
    connect = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    coord_id = models.OneToOneField(Coord, on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)


class Images(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    data = models.URLField(verbose_name='Изображение', null=True, blank=True)
    pereval_id = models.ForeignKey(Pereval, related_name='photo', on_delete=models.CASCADE)

