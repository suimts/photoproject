# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
import bootstrap_datepicker_plus.widgets as datetimepicker
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス
        
        Attributes:
          model: 連携するUserモデル
          fields: フォームで使用するフィールド
        '''
        # 連携するUserモデルを設定
        model = CustomUser
        # フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、ニックネーム、誕生日、パスワード、パスワード(確認用)
        fields = ('username', 'email', 'nickname', 'birth_date', 'password1', 'password2')
        labels = {
            'nickname': 'ニックネーム',
            'birth_date': '誕生日',
            'password1': 'パスワード',
            'password2': 'パスワード(確認用)',
        }
        widgets = {
            'birth_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and "example.com" in email:
            raise ValidationError("適切なメールアドレスを入力してください。")

        return email

    def clean(self):
        cleaned_data = super().clean()

        # Additional cleaning logic can be added here if needed

        return cleaned_data
