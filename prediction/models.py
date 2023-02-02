from django.db import models
from .choices import sext,trestbpst,fbst,exangt,targett,restecgt,cpt,thalt,cat
from django.utils.translation import  gettext as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
# Create your models here.
class Prediction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    age=models.IntegerField(_("age"))
    sex=models.BooleanField(_("sex"),choices=sext,max_length=50)
    cp=models.IntegerField(_("cp"),choices=cpt)
    trestps=models.IntegerField(_("trestbps"))
    restecg=models.BooleanField(_("restecg"),choices=restecgt,default=1)
    chol=models.IntegerField(_("chol"))
    fbs=models.BooleanField(_("fbs"),choices=fbst)
    thalach=models.IntegerField(_("thalach"))
    exang=models.BooleanField(_("exang"),choices=exangt)
    oldpeak=models.FloatField(_("oldpeak"))
    slope=models.IntegerField(_("slope"))
    ca=models.IntegerField(_("ca"),choices=cat)
    thal=models.IntegerField(_("thal"),choices=thalt)
    upload_date=models.DateTimeField(default=datetime.now,blank=True)
    target=models.BooleanField(_("target"),choices=targett,null=True)

    def __str__(self):
        return self.first_name