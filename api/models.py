# -- coding: utf-8 --
from django.contrib.auth.models import User,  Group, Permission
from django.db import models

class WifiUsers(User):
   class Meta:
       db_table = 'Users'
       verbose_name_plural = 'Пользователи'
   roleusers = (
               ('admin', 'Админ'),
               ('owner', 'Собственник Заведения'),
               ('manager', 'Менеджер Заведения'),
               ('user', 'Посетитель'),
               )
   role = models.CharField(max_length=30, choices=roleusers, default='user', verbose_name = 'тип учетной записи')
   companyName = models.CharField(max_length=100, verbose_name = 'компания клиента', blank=True, null=True)
   address = models.CharField(max_length=200, verbose_name = 'адрес клиента',)
   phone = models.CharField(max_length=100, verbose_name = 'телефон клиента',)
   additional = models.TextField(verbose_name = 'Информация о клиенте, примечания', blank=True, null=True) 
   def __unicode__(self):
        return '%s %s  %s' % (self.firstName, self.lastName, self.companyName)

class AdvertisingCampaign(models.Model):
   class Meta:
       db_table = 'Advertising Campaign'
       verbose_name_plural = 'Рекламные компании'
   user = models.ForeignKey(WifiUsers)
   nameCompaign = models.CharField(max_length=300, verbose_name = 'имя рекламной компании',)
   banner = models.CharField(max_length=300, verbose_name = 'имя баннера для показа',)
   desCompaign = models.TextField(verbose_name = 'Информация о рекламной компании', blank=True, null=True)
   countShows = models.IntegerField(verbose_name = 'Колличество показов в рекламной компании',)
   showsPeerUser = models.IntegerField(verbose_name = 'Колличество показов на пользователя',)
   showsInterval = models.IntegerField(verbose_name = 'интервал показов в минутах',)
   https = models.BooleanField(default=False, verbose_name = 'Показывать на https', )
   def __unicode__(self):
       return self.nameCompaign
class WifiShows(models.Model):
   class Meta:
       db_table = 'Shows Info'
       verbose_name_plural = 'Показы'
   user = models.ForeignKey(AdvertisingCampaign)
   dateShow = models.DateTimeField(auto_now=True, verbose_name ='Дата показа',)
   nameCompaign = models.CharField(max_length=300, verbose_name = 'имя рекламной компании',)
   def __unicode__(self):
       return ('%s %s') % (self.name_compaign, date_show)  
   
