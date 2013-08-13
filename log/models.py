from django.db import models

class Facilities(models.Model):
    id = models.IntegerField(primary_key=True)
    facility = models.CharField(max_length=84)
    def __unicode__(self):
        return self.facility
    class Meta:
        db_table = u'Facilities'

class Priorities(models.Model):
    num = models.IntegerField(primary_key=True)
    severity = models.CharField(max_length=54)
    def __unicode__(self):
        return self.severity
    class Meta:
        db_table = u'Priorites'

class Event(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    customerid = models.BigIntegerField(db_column='CustomerID', null=True, blank=True)
    receivedat = models.DateTimeField(db_column='ReceivedAt', null=True, blank=True)
    devicereportedtime = models.DateTimeField(db_column='DeviceReportedTime', null=True, blank=True)
    facility = models.OneToOneField(Facilities, db_column='facility', to_field='id')
    priority = models.OneToOneField(Priorities, db_column='priority', to_field='num')
    fromhost = models.CharField(db_column='FromHost', max_length=180, blank=True)
    message = models.TextField(db_column='Message', blank=True)
    ntseverity = models.IntegerField(db_column='NTSeverity', null=True, blank=True)
    importance = models.IntegerField(db_column='Importance', null=True, blank=True)
    eventsource = models.CharField(db_column='EventSource', max_length=180, blank=True)
    eventuser = models.CharField(db_column='EventUser', max_length=180, blank=True)
    eventcategory = models.IntegerField(db_column='EventCategory', null=True, blank=True)
    eventid = models.IntegerField(db_column='EventID', null=True, blank=True)
    eventbinarydata = models.TextField(db_column='EventBinaryData', blank=True)
    maxavailable = models.IntegerField(db_column='MaxAvailable', null=True, blank=True)
    currusage = models.IntegerField(db_column='CurrUsage', null=True, blank=True)
    minusage = models.IntegerField(db_column='MinUsage', null=True, blank=True)
    maxusage = models.IntegerField(db_column='MaxUsage', null=True, blank=True)
    infounitid = models.IntegerField(db_column='InfoUnitID', null=True, blank=True)
    syslogtag = models.CharField(db_column='SysLogTag', max_length=180, blank=True)
    eventlogtype = models.CharField(db_column='EventLogType', max_length=180, blank=True)
    genericfilename = models.CharField(db_column='GenericFileName', max_length=180, blank=True)
    systemid = models.IntegerField(db_column='SystemID', null=True, blank=True)
    def __unicode__(self):
        return self.message
    class Meta:
        db_table = u'SystemEvents'

class EventProps(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    systemeventid = models.IntegerField(null=True, db_column='SystemEventID', blank=True)
    paramname = models.CharField(max_length=180, db_column='ParamName', blank=True)
    paramvalue = models.TextField(db_column='ParamValue', blank=True)
    def __unicode__(self):
        return self.paramname
    class Meta:
        db_table = u'SystemEventsProperties'

