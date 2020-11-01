from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime

# Create your views here.
from blog.form  import PersonInfo
from django.shortcuts import redirect
from blog.models import Person
def index(request):
# generic view
# 
    if request.method=="POST":
        form = PersonInfo(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = PersonInfo()  
        print(request)
    return render(request, 'index.html',{'form':form})

        # fname1 = request.POST['fname12']
        # lname1 = request.POST['lname']
        # email1 = request.POST['email']
        # state1 = request.POST['state']
        # city1 = request.POST['city']
        # contact1 = request.POST['contact']
        # postalcode1 = request.POST['postalcode']
        # pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']

        # if fname1=='':
        #     return HttpResponse("Your First Name is None...! SO try to fill it..! Thankyou...!")
        

        # if lname1=='':
        #     return HttpResponse("Your Last Name is None...! SO try to fill it..! Thankyou...!")
        

        # if email1=='':
        #     return HttpResponse("Your email address is None...! SO try to fill it..! Thankyou...!")
        

        # if state1=='':
        #     return HttpResponse("Your state name is None...! SO try to fill it..! Thankyou...!")
        

        # if city1=='':
        #     return HttpResponse("Your city name is None...! SO try to fill it..! Thankyou...!")
        

        # if contact1=='':
        #     return HttpResponse("Your contact Number is None...! SO try to fill it..! Thankyou...!")
        

        # if len(contact1)<13:
        #     return HttpResponse("Your contact Number is greater then 14 try to fill with your country code..! Thankyou")
        

        # if postalcode1=='':
        #     return HttpResponse("Your postal code name is None...! SO try to fill it..! Thankyou...!")
        




        # check for errorneous input
        # if len(username)<10:
        #     return HttpResponse("Your user name must be under 10 characters")
            # messages.error(request, " Your user name must be under 10 characters")
            # return redirect('home')

        # if not username.isalnum():
        #     return HttpResponse(" User name should only contain letters and numbers")
            # messages.error(request, " User name should only contain letters and numbers")
            # return redirect('home')
        # elif (pass1!= pass2):
        #     return HttpResponse(" Passwords do not match")
        #     #  messages.error(request, " Passwords do not match")
        
        # Create the user
        # myuser = Person(fname= fname1 , lname=lname1,email = email1, state = state1, city = city1, contact=contact1, postalcode=postalcode1, password=pass1)
        # myuser.save()
        # return HttpResponse("Your iCoder has been successfully created")
        # messages.success(request, " Your iCoder has been successfully created")
        # return redirect('home')

    # return render(request, 'index.html')


def signin(request):  
    if request.method=="POST":
        ema = Person.objects.filter(id=id)
        print('hello===============>')
        email1 = request.POST['email']
        pass2 = request.POST['pass2']
        if email==ema:
            print(ema)
            print(email)
            return HttpResponse("your email has matched")

    return render(request,"signin.html")          