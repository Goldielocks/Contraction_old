from django.apps import AppConfig

class CaseConfig(AppConfig):
	name = 'Case'

	def ready(self):
		Case = self.get_model('Case')