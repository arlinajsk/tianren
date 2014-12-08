# -*- coding: utf-8 -*-

from django.db import models
from tianren.datamodel.enums import MONTHS, DATES, HOURS, GENDER, ROUTINE_FREQUENCY, LANGUAGES, TRANSPORT
from tianren.lib.multiselectfield.db.fields import MultiSelectField

class Temple( models.Model ):
    templeId    = models.AutoField(primary_key=True)
    templeName  = models.CharField(max_length=128, verbose_name=u'佛堂')
    address1    = models.CharField(max_length=128)
    address2    = models.CharField(max_length=128, blank=True, null=True)
    city        = models.CharField(max_length=64)
    state       = models.CharField(max_length=2)
    zipCode     = models.IntegerField()
    
    def __unicode__( self ):
        return self.templeName
    
class People( models.Model ):
    personId    = models.AutoField(primary_key=True)
    lastName    = models.CharField(max_length=64)
    firstName   = models.CharField(max_length=64)
    chineseName = models.CharField(max_length=64, blank=True, verbose_name=u'中文名')
    gender      = models.CharField(max_length=1, choices=GENDER, default='M', verbose_name=u'乾/坤')
    address1    = models.CharField(max_length=128)
    address2    = models.CharField(max_length=128, blank=True, null=True)
    city        = models.CharField(max_length=64)
    state       = models.CharField(max_length=2)
    zipCode     = models.CharField(max_length=10, verbose_name='zip code ( 5 or 9 digits)')
    homePhone   = models.CharField(max_length=10, blank=True, null=True)
    cellPhone   = models.CharField(max_length=10, blank=True, null=True)
    email       = models.EmailField(blank=True)
    language    = MultiSelectField(max_length=64, blank=True, null=True, choices=LANGUAGES )
    transport   = MultiSelectField(max_length=16, blank=True, null=True, choices=TRANSPORT, verbose_name=u'交通' )
    notes       = models.TextField(blank=True)

    def __unicode__( self ):
        return u'{0},{1} ( {2} )'.format( self.lastName, self.firstName, self.chineseName )

class Initiation( models.Model ):
    personId                = models.ForeignKey( People, primary_key=True )
    initiationDate          = models.DateField(verbose_name='西元')
    initiationChineseYear   = models.CharField(max_length=8, verbose_name='歲次')
    initiationChineseMonth  = models.CharField(max_length=2, choices=MONTHS, verbose_name='月')
    initiationChineseDay    = models.CharField(max_length=2, choices=DATES, verbose_name='日')
    initiationChineseHour   = models.CharField(max_length=2, choices=HOURS, verbose_name='時辰')
    templeName              = models.ForeignKey( Temple )
    dianChuanShr            = models.CharField(max_length=8, verbose_name='點傳師')
    introductor             = models.ForeignKey( People, related_name='initiation_introductor', verbose_name='引師' )
    guarantor               = models.ForeignKey( People, related_name='initiation_guarantor', verbose_name='保師')
    donationAmount          = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='功德費')
    initiationNotes         = models.TextField(blank=True, null=True)
    
    def __unicode__( self ):
        return u'{0}, {1}, {2}, {3}, {4}'.format( self.personId, self.initiationDate, self.introductor, self.guarantor, self.dianChuanShr  ) 
    
class Donation( models.Model ):
    donationId          = models.AutoField(primary_key=True)
    personId            = models.ForeignKey( People )
    donationDate        = models.DateField()
    donationAmount      = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='功德費')
    routineDonation     = models.NullBooleanField(default='No')
    routineFrequency    = models.CharField( max_length=2, choices=ROUTINE_FREQUENCY, blank=True, null=True)
    donationNotes       = models.TextField(blank=True, null=True)
    
    def __unicode__( self ):
        return u'{0}, {1}, {2}, {3}'.format( self.donationId, self.personId, self.donationDate, self.donationAmount )
        
        