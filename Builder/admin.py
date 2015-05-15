from django.contrib import admin
from Builder.models import Article, Node, Category, Clause, ClauseProbability
import reversion

class NodeAdmin(reversion.VersionAdmin):

	pass

class ArticleAdmin(reversion.VersionAdmin):

	pass	

admin.site.register(Node, NodeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Clause)
admin.site.register(ClauseProbability)


