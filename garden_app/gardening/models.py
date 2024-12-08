from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    garden_size = models.FloatField()
    location = models.CharField(max_length=255)
    preferred_plants = models.TextField()
    experience_level = models.CharField(max_length=100, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    gardening_interests = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    growth_conditions = models.TextField()

    def __str__(self):
        return self.name


class PlantGrowth(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date_planted = models.DateField()
    growth_log = models.TextField()
    photo = models.ImageField(upload_to='plant_photos/')

    def __str__(self):
        return f"{self.plant.name} Growth Record"


class Task(models.Model):
    plant_growth = models.ForeignKey(PlantGrowth, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.plant_growth.plant.name} due on {self.due_date}"


class CommunityPost(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user_profile.user.username} on {self.created_at}"


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
