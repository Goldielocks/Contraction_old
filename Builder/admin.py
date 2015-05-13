from django.contrib import admin
from Builder.models import Agreement, Node, Category, Clause, ClauseProbability
import reversion

class NodeAdmin(reversion.VersionAdmin):

	pass

class AgreementAdmin(reversion.VersionAdmin):

	pass	

admin.site.register(Node, NodeAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Category)
admin.site.register(Clause)
admin.site.register(ClauseProbability)


