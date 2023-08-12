# from django import forms
# from .models import User
# from django.contrib.auth.password_validation import validate_password


# class RegistForm(forms.ModelForm):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(label="確認用password",widget=forms.PasswordInput)
    
#     class Meta():
#         model = User
#         fields = ("username", "password")
        
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     password = cleaned_data["password"]
#     #     confirm_password = cleaned_data["confirm_password"]
#     #     if password != confirm_password:
#     #         raise forms.ValidationError('パスワードが違います')
        
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("パスワードが一致しません")

    
#     def save(self, commit=False):
#         user = super().save(commit=False)
#         validate_password(self.cleaned_data['password'], user)
#         user.set_password(self.cleaned_data['password'])
#         user.save()
#         return user