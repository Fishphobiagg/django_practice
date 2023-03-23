from django.db import models

# Create your models here.
class Todo(models.Model):
    '''
    어떤 필드가 필요할지 생각
    task = charfield 채택
    created_at = datafield # 생성시간
    completed_at = datafield # 완료시간
    isCompleted = False 채택
    inProgress = True

    '''

    task         = models.CharField(max_length=300)
    isCompleted  = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)