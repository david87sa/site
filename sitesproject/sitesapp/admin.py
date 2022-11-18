from django.contrib import admin

from .models import Owner
from .models import Site
from .models import Section
from .models import Component
from .models import ComponentRenderer
from .models import SectionRenderer
from .models import Theme
from .models import Guest

# Register your models here.
admin.site.register(Owner)
admin.site.register(Site)
admin.site.register(Section)
admin.site.register(Component)
admin.site.register(SectionRenderer)
admin.site.register(ComponentRenderer)
admin.site.register(Theme)
admin.site.register(Guest)
