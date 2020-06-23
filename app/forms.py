from django import forms

gender=(('male','male'),('female','female'))
#('what u have to carry as an output to database','What to dislpay in form')
course=(('python','python'),('django','django'))
class New_Form(forms.Form):
    #name=forms.CharField(max_length=10,min_length=5,label='LAST',label_suffix='NAME',help_text='Enter Ur Name')
    #number=forms.IntegerField(max_value=100,min_value=25,required=False)
    #url=forms.URLField(max_length=30)
    #email=forms.EmailField(min_length=5)
    #comments=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    #gender1=forms.ChoiceField(choices=gender)
    #gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=course)
    #check=forms.MultipleChoiceField(choices=course,widget=forms.CheckboxSelectMultiple)
    time=forms.TimeField()# 24 hr format
    date=forms.DateField()#yyyy-mm-dd
    datetime=forms.DateTimeField()#yyyy-mm-dd hr:min
    
    