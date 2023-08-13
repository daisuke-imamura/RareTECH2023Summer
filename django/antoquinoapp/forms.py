from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe





class RegistForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ("username", "password")
        

    def clean(self):
            cleaned_data = self.cleaned_data
            username = cleaned_data.get("username")
            password = cleaned_data.get("password")
            
            if username and password:
                # データベースから既に登録済みのユーザー情報を取得する例（Django ORMを使用）
                existing_user = User.objects.filter(username=username, password=password).first()
                
                if existing_user:
                    raise ValidationError("そのパスワードは使えません。")
            
            return cleaned_data
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    

class Loginform(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        if username and password:
            # データベースから既に登録済みのユーザー情報を取得する例（Django ORMを使用）
            existing_user = User.objects.filter(username=username).first()
            
            if existing_user and not existing_user.check_password(password):
                raise forms.ValidationError("ユーザー名とパスワードが一致しません。")
        
        return cleaned_data
    
    

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'category', 'ingredients']  # 作成したいフィールドを指定

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-select'  # カテゴリーフィールドにCSSクラスを追加

        