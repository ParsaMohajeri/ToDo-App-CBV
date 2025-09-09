from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from accounts.models import User
from work.models import Task
from datetime import datetime
import random
from .utils import random_date



class Command(BaseCommand):
    help = "Inserting dummy data"

    def __init__(self, *args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake =Faker()
    def handle(self, *args, **options):
        user= User.objects.create( email= self.fake.email(),username=self.fake.first_name(),password="text@1234567")
        

        for _ in range(5):
            Task.objects.create(
                author = user,
                is_done = random.choice([True,False]),
                title = self.fake.paragraph(nb_sentences=1),
                content = self.fake.paragraph(nb_sentences = 10),
                deadline = random_date,
                )



