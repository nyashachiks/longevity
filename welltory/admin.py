from django.contrib import admin
from django.contrib import admin
from .models import (BioMarker,
                     Parameter,
                     Reading,
                     Disease,
                     Recommendation,
                     Practitioner,
                     Patient)

# Register your models here.
admin.site.register(BioMarker)
admin.site.register(Parameter)
admin.site.register(Reading)
admin.site.register(Disease)
admin.site.register(Recommendation)
admin.site.register(Practitioner)
admin.site.register(Patient)

