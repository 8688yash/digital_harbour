from django.contrib import admin
from .models import UserProfile, Skill, Certificate, Post, Message

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Post)
admin.site.register(Message)
