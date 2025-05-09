import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from django.contrib.auth.models import User
from community.models import UserProfile, Skill, Post, Message

fake = Faker()

skills = ['Python', 'Django', 'AI', 'UI/UX', 'DevOps', 'JavaScript']

def create_skills():
    for name in skills:
        Skill.objects.get_or_create(name=name)

def create_users(n):
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        profile = UserProfile.objects.create(user=user, bio=fake.text())
        profile.skills.set(random.sample(list(Skill.objects.all()), k=2))
        profile.save()

def create_posts():
    for user in User.objects.all():
        for _ in range(random.randint(1, 3)):
            Post.objects.create(
                author=user,
                content=fake.sentence()
            )

def create_messages():
    users = list(User.objects.all())
    for _ in range(30):
        sender = random.choice(users)
        receiver = random.choice([u for u in users if u != sender])
        Message.objects.create(
            sender=sender,
            receiver=receiver,
            text=fake.sentence()
        )

if __name__ == '__main__':
    create_skills()
    create_users(10)
    create_posts()
    create_messages()
    print("Dummy data created.")
