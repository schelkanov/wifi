# -- coding: utf-8 --
from django.contrib.auth.models import User,  Group, Permission
from django.db import models

class WifiUsers(models.Model):
   class Meta:
       db_table = 'Users'
       verbose_name_plural = 'Пользователи'
   id  = models.AutoField(primary_key=True)
   first_name = models.CharField(max_length=40, verbose_name = 'имя клиента',)
   last_name = models.CharField(max_length=40, verbose_name = 'фамилия клиента',)
   company_name = models.CharField(max_length=100, verbose_name = 'компания клиента', blank=True, null=True)
   address = models.CharField(max_length=200, verbose_name = 'адрес клиента',)
   create_date = models.DateTimeField(auto_now=True, verbose_name ='дата регистрации клиента',)
   phone = models.CharField(max_length=100, verbose_name = 'телефон клиента',)
   email = models.CharField(max_length=100, verbose_name = 'мыло клиента', blank=True, null=True)
   info = models.TextField(verbose_name = 'Информация о клиенте, примечания', blank=True, null=True) 
   password = models.CharField(max_length=500, verbose_name = 'пароль md5',)
   def __unicode__(self):
        return '%s %s  %s' % (self.first_name, self.last_name, self.company_name)

class AdvertisingCampaign(models.Model):
   class Meta:
       db_table = 'Advertising Campaign'
       verbose_name_plural = 'Рекламные компании'
   user = models.ForeignKey(WifiUsers)
   name_compaign = models.CharField(max_length=300, verbose_name = 'имя рекламной компании',)
   banner = models.CharField(max_length=300, verbose_name = 'имя баннера для показа',)
   desc_compaign = models.TextField(verbose_name = 'Информация о рекламной компании', blank=True, null=True)
   count_shows = models.IntegerField(verbose_name = 'Колличество показов в рекламной компании',)
   shows_peer_user = models.IntegerField(verbose_name = 'Колличество показов на пользователя',)
   shows_interval = models.IntegerField(verbose_name = 'интервал показов в минутах',)
   def __unicode__(self):
       return self.name_compaign
class WifiShows(models.Model):
   class Meta:
       db_table = 'Shows Info'
       verbose_name_plural = 'Показы'
   user = models.ForeignKey(AdvertisingCampaign)
   date_show = models.DateTimeField(auto_now=True, verbose_name ='Дата показа',)
   name_compaign = models.CharField(max_length=300, verbose_name = 'имя рекламной компании',)
   def __unicode__(self):
       return ('%s %s') % (self.name_compaign, date_show)  
   
