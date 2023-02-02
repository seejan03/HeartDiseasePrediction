from django.shortcuts import render,redirect,get_object_or_404
from .models import Prediction
from django.contrib import messages
from .choice import sext,trestbpst,fbst,exangt,targett,restecgt,cpt,thalt,cat,slopet
from .naive import *
from django.http import HttpResponse
from .middlewares.authmiddleware import simple_middleware
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/account/login')
def addpredict(request):
    if request.method=="POST":

        age=float(request.POST['Age'])
        sex=float(request.POST['sex'])
        cp=float(request.POST['cp'])
        trestps=float(request.POST['RestBPS'])
        restecg=float(request.POST['restecg'])
        chol=float(request.POST['Cholestrol'])
        fbs=float(request.POST['fbs'])
        thalch=float(request.POST['Thalach'])
        exang=float(request.POST['exang'])
        oldpeak=float(request.POST['oldpeak'])
        slope=float(request.POST['slope'])
        ca=float(request.POST['ca'])
        thal=float(request.POST['thal'])

        if request.user.is_authenticated:
            target = make_prediction([[
                age, sex, cp, trestps,chol,fbs, restecg,   thalch, exang, oldpeak, slope, ca, thal
            ]])
            prediction=Prediction(user=request.user,age=age,sex=sex,cp=cp,trestps=trestps,restecg=restecg,chol=chol,fbs=fbs,thalach=thalch,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal, target = target)
            prediction.save()
            messages.success(request, "Your prediction has been submitted to the concerned one")
            context = {
                'prediction': prediction
            }
            return render(request, 'predictionform/viewprediction.html', context)
        else:
            return redirect('login')

    else:
        context={
            'cpt':cpt,
            'sext':sext,
            'trestbpst':trestbpst,
            'fbst':fbst,
            'restecgt':restecgt,
            'exangt':exangt,
            'thalt':thalt,
            'cat':cat,
            'slopet':slopet,
        }
        return render(request,'predictionform/from.html',context)


def predict(request,prediction_id):


        prediction=get_object_or_404(Prediction,pk=prediction_id)
        user=prediction.user.id
        if user==request.user.id:
            context={
                'prediction':prediction
            }
            return render(request,'predictionform/viewprediction.html',context)
        else:
            return HttpResponse("Unauthorized", status=401)
@login_required(login_url='/account/login')
def prediction_history(request):
    if request.user.is_authenticated:
        prediction=Prediction.objects.filter(user=request.user).order_by('-upload_date')
        context={
        'prediction':prediction
        }
        return render(request,'predictionform/predictionhistory.html',context)
    else:
        messages.error(request,'You must login to your account first')
        return redirect('login')