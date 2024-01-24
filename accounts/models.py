from django.db import models

# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザーモデル
    '''
    nickname = models.CharField(max_length=50, blank=True, null=False)
    hobbies = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    pass
