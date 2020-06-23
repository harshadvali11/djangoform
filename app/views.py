from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app import forms

def New_Form(request):
    form=forms.New_Form()#sending form input elments without data
    if request.method=='POST':
        form_data=forms.New_Form(request.POST)
        if form_data.is_valid():
            #print(form_data.cleaned_data)
            #return HttpResponse('form submitted successfully')
            #name=form_data.cleaned_data['name']#directly by keyname
            #number=form_data.cleaned_data.get('number')#using get method
            #url=form_data.cleaned_data.get('url')
            #email=form_data.cleaned_data['email']
            #gender=form_data.cleaned_data['gender']
            #courses=form_data.cleaned_data['courses']
            #check=form_data.cleaned_data['check']
            time=form_data.cleaned_data['time']#24 hr format
            date=form_data.cleaned_data['date']
            datetime=form_data.cleaned_data['datetime']
            #d={'name':name,'number':number,'url':url,'email':email,'gender':gender,'courses':courses,'check':check}
            d1={'time':time,'date':date,'datetime':datetime}
            return render(request,'formdata.html',context=d1)

    return render(request,'New_Form.html',context={'form':form})



