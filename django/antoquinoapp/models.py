from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import BaseUserManager



# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')

#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    stocks = models.TextField(verbose_name="食材メモ",unique=False, null=True)
    
    # objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        
class Recipe(models.Model):
    CATEGORY_CHOICES = (
        ('鶏肉', '鶏肉'),
        ('牛肉', '牛肉'),
        ('豚肉', '豚肉'),
        ('麺類', '麺類'),
        ('魚', '魚'),
        ('野菜', '野菜'),
        ('ご飯物', 'ご飯物'),
        ('その他', 'その他'),
    )
    
    recipe_name = models.CharField(max_length=255, verbose_name="料理名")
    # photo_url = models.TextField(verbose_name="画像アップロード",unique=False, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES,unique=False, null=True)
    ingredients = models.TextField(verbose_name="材料",unique=False, null=True)
    created_at= models.DateField(verbose_name="作成日",auto_now_add=True)
    favorire = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.recipe_name
    
    class Meta:
        db_table = 'recipes'
        

class Step(models.Model):
    step_number = models.PositiveIntegerField(verbose_name="手順",unique=False, null=True)
    description = models.TextField(verbose_name="説明",unique=False, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.step_number)
    
    class Meta:
        db_table = 'steps'


# class UserActivateTokens(models.Model):
    
#     token = models.UUIDField(db_index=True)
#     expired_at = models.DateTimeField()
#     user = models.ForeignKey(
#         'User', on_delete=models.CASCADE
#     )
    
#     class Meta:
#         db_table = 'user_activate_tokens'
        