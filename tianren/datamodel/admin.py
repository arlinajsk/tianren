# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from tianren.datamodel.models import People, Initiation, Temple, Donation



class InitiationAdmin( admin.ModelAdmin ):
    list_display = ('personId', 'initiationDate', 'introductor', 'guarantor', 'dianChuanShr')

class DonationAdmin( admin.ModelAdmin ):
    list_display = ( 'donationId', 'personId', 'donationDate', 'donationAmount' )

class PeopleAdmin( admin.ModelAdmin ):
    list_display = ('lastName', 'firstName', 'chineseName')

class TempleAdmin( admin.ModelAdmin ):
    list_display = ( 'templeName',  )


admin.site.register( People, PeopleAdmin )
admin.site.register( Initiation, InitiationAdmin )
admin.site.register( Donation, DonationAdmin )
admin.site.register( Temple, TempleAdmin )

# class InitiationAdminSite( AdminSite ):
#     site_header = u'求道 - 名單 (Initiation)'
    
# class PeopleAdminSite( AdminSite ):
#     site_header = u'人 - 名單 (Contacts)'    
    
# class DonationAdminSite( AdminSite ):
#     site_header = u'捐款 - 名單 (Donations)'    
    
# class TempleAdminSite( AdminSite ):
#     site_header = u'佛堂 - 名單 (Temple)'    
    
# initiation_admin_site = InitiationAdminSite( name='initiation_admin' )
# initiation_admin_site.register( Initiation, InitiationAdmin )
    
# people_admin_site = PeopleAdminSite( name='people_admin' )
# people_admin_site.register( People, PeopleAdmin )

# donation_admin_site = DonationAdminSite( name='donation_admin' )
# donation_admin_site.register( Donation, DonationAdmin )

# temple_admin_site = TempleAdminSite( name='temple_admin' )
# temple_admin_site.register( Temple, TemplenAdmin )







