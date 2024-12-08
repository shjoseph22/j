# from django.contrib import admin
# # from .models import UserProfile, Plant, PlantGrowth, Task, CommunityPost, Tutorial, Challenge
#
# # Register your models here
#
# # @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'garden_size', 'location', 'experience_level')
#     search_fields = ('user__username', 'location')
#
# @admin.register(Plant)
# class PlantAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#
# @admin.register(PlantGrowth)
# class PlantGrowthAdmin(admin.ModelAdmin):
#     list_display = ('user_profile', 'plant', 'date_planted')
#     list_filter = ('user_profile', 'plant')
#     search_fields = ('user_profile__user__username', 'plant__name')
#
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('plant_growth', 'task_type', 'due_date', 'completed')
#     list_filter = ('completed', 'due_date')
#     search_fields = ('task_type',)
#
# @admin.register(CommunityPost)
# class CommunityPostAdmin(admin.ModelAdmin):
#     list_display = ('user_profile', 'created_at')
#     search_fields = ('user_profile__user__username', 'content')
#
# @admin.register(Tutorial)
# class TutorialAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title',)
#
# @admin.register(Challenge)
# class ChallengeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title',)
#
# # Optionally, you can customize admin behavior further by adding more configurations
