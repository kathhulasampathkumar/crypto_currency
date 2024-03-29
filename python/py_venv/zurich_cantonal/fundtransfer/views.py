from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt 
from user_master.models import user_master ,CurrencyExchange

# Create your views here.
def login_page (request):
    if 'user_id' in request.session:
        del request.session['user_id']  # or request.session.pop('user_id', None)    
        context={'title':'Home'}
        return render(request,'index_form.html',context)
    else :
        # del request.session['user_id']  # or request.session.pop('user_id', None)    
        context={'title':'Home'}
        return render(request,'index_form.html',context)
def home(request):    
    user_id=request.session.get('user_id')
    context={'title':'HomePage','user_id':user_id}
    return render(request,'index.html',context)
def getUserData(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)        
        if user_master.objects.filter(email=email,password=password,status=1).exists():
            user = user_master.objects.filter(email=email,password=password,status=1).get()
            if user.id is not None :
                request.session['user_id']=user.id   
                user_id = request.session.get('user_id') 
                context={'title':'HomePage','user_id':user_id}
                return render(request,'dashboard.html',context)
            else :
                messages.add_message(request,messages.WARNING,'Invalid Credentials. Please enter valid credentials.')
                return redirect('login_page')
        else :
            messages.add_message(request,messages.WARNING,'Invalid Credentials. Please enter valid credentials.')
            return redirect('login_page')
    else :
        return redirect('login_page')
from decimal import Decimal
@csrf_exempt  
def getCurrValues(request):
    if request.session.get('user_id') is not None :
        user_id = request.session.get('user_id')
        user = user_master.objects.filter(status=1,id=user_id).get()
        curRates=CurrencyExchange.objects.all()
        for rate in curRates :
            if rate.id == 1:
                UsdCurrVal = ((user.balance) / Decimal(rate.from_val)).quantize(Decimal('1.0000'))
            if rate.id == 2:
                BtcCurrVal = ((user.balance) / Decimal(rate.from_val)).quantize(Decimal('1.000000000'))
            if rate.id == 3:
                InrCurrVal = ((user.balance) / Decimal(rate.from_val)).quantize(Decimal('1.0'))
        print(str(InrCurrVal)+str(UsdCurrVal)+str(BtcCurrVal))
        
        # print(curRates)
        context={
            "InrCurrVal": InrCurrVal,
            "UsdCurrVal": UsdCurrVal,
            "BtcCurrVal": BtcCurrVal,
        }
        # context={
        #     "InrCurrVal":(user.balance * 1),
        #     "UsdCurrVal":(user.balance * 78),
        #     "BtcCurrVal":(user.balance) /(1000000028),
        # }
        # context = {
        #     "InrCurrVal": user.balance.quantize(Decimal('1.00')),
        #     "UsdCurrVal": (user.balance * Decimal('78')).quantize(Decimal('1.0000')),
        #     "BtcCurrVal": (user.balance / Decimal('1000000028')).quantize(Decimal('1.000000000')),
        # }
        return JsonResponse(context,safe = False)
        # return render(request,'dashboard.html',context)





    # return HttpResponse('you are requested homepage')
