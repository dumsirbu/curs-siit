from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        args = super().add_arguments(parser)
        parser.add_argument('an', type=int)
        parser.add_argument('--dry-run', type=bool, required=False)

    def handle(self, *args, **options):
        print("Args", args)
        print("Kwargs", options)

    def must_implement(self):
        raise NotImplementedError()