from django.core.management.base import BaseCommand, CommandError
from django.db.models import F

from curs.models import Student

class Command(BaseCommand):

    def add_arguments(self, parser):
        args = super().add_arguments(parser)
        parser.add_argument('--an', type=int, required=False)
        parser.add_argument('--dry-run', type=bool, required=False)

    def handle(self, *args, **options):
        queryset = Student.objects.all()
        if options['an'] is not None:
            queryset = queryset.filter(an=options['an'])
        rows_modified = queryset.update(an=F('an') + 1)
        if rows_modified == 0:
            raise CommandError("Nu am modificat nici un rand")
        print(f"Am modificat {rows_modified} studenti")

    def must_implement(self):
        raise NotImplementedError()