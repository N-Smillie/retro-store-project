from django.db import models

# Create your models here.
class Game(models.Model):
    CONSOLE_CHOICES = [
        ('NES', 'NES'),
        ('SNES', 'SNES'),
        ('N64', 'N64'),
        ('PS1', 'PlayStation 1'),
        ('GB', 'Game Boy'),
        ('XBOX', 'Xbox'),
    ]

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('rpg', 'RPG'),
        ('sports', 'Sports'),
        ('puzzle', 'Puzzle'),
        ('platformer', 'Platformer'),
        ('racing', 'Racing'),
    ]

    title = models.CharField(max_length=200)
    console = models.CharField(max_length=10, choices=CONSOLE_CHOICES)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='games/')

    def __str__(self):
        return f"{self.title} ({self.console})"
    
class GradedItem(models.Model):

    GRADE_CHOICES = [
        ('10.0', 'Mint 10.0'),
        ('9.8', '9.8'),
        ('9.6', '9.6'),
        ('9.4', '9.4'),
        ('9.2', '9.2'),
        ('9.0', '9.0'),
    ]

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='graded_items'
    )

    grade = models.CharField(max_length=5, choices=GRADE_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)

    slab_image = models.ImageField(upload_to='graded_items/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.title} - {self.grade}"