# yourapp/lookups.py
from ajax_select import register, LookupChannel
from .models import Worker

@register('workers')
class TagsLookup(LookupChannel):

    model = Worker

    def get_query(self, q, request):
        return self.model.objects.filter(firstname__icontains=q).order_by('firstname')[:50]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.firstname