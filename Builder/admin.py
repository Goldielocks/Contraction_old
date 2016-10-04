from django.contrib import admin
from Builder.models import Contract, Node, Category, Clause, ClauseProbability, Family
from reversion.admin import VersionAdmin

class NodeAdmin(VersionAdmin):

	pass

class ContractAdmin(VersionAdmin):

	pass	

admin.site.register(Node, NodeAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Category)
admin.site.register(Clause)
admin.site.register(ClauseProbability)
admin.site.register(Family)

