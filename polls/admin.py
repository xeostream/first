from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['pud_date'], 'classes': ['collapse']}),
	]
	list_display = ('question', 'pud_date', 'was_published_recently')
	list_filter = ['pud_date']
	search_fields = ['question']
	date_hierarchy = 'pud_date'

admin.site.register(Poll, PollAdmin)