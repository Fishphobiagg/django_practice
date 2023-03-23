from django import forms
from .models import Todo

'''
Django Form VS ModelForm
Form : html 랜더링, 유효성 검사 <- 귀찮다. django야 대신해라 형 짬에 내가 해야겠냐?
ModelForm : 어차피 form 객체 DB와 같이 쓸건데, 필드도 model 기반으로 만들어줘. 형 짬에 내가 해야겠냐?
'''

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo # 이 모델 기반으로 Form을 만들어줘
        fields = ('task',) # 모든 필드 다 받아라
        # fields or exclude 둘중 하나만 사용하는거 권장

