from django.contrib import admin
from Builder.models import Case, Citation
import reversion

class CaseAdmin(reversion.VersionAdmin):

	pass


admin.site.register(Case, CaseAdmin)
admin.site.register(Citation)

