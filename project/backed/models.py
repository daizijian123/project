from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '用户'
        
    status = models.IntegerField(default=0, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100, verbose_name='姓名')
    password = models.CharField(null=True,max_length=200, verbose_name='密码')