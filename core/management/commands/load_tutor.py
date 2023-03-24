from django.core.management.base import BaseCommand
from core.models import Tutor, Module
from faker import Faker


class Command(BaseCommand):
    help = 'Load Tutors'

    def handle(self, *args, **kwargs):
        # for each module, add 3 tutors
        faker = Faker()
        for module in Module.objects.all():
            for i in range(3):
                # create the tutor
                Tutor.objects.create(
                    name=faker.name(),
                    module=module
                )
