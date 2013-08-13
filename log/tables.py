import django_tables2 as tables
from log.models import Event

class EventTable(tables.Table):
    class Meta:
        model = Event
        attrs = {'class': 'paleblue'}
        fields = ('id','devicereportedtime','fromhost','facility','priority','message')
        sequence = ('id','devicereportedtime','fromhost','facility','priority','message')
        order_by = ('-id',)
