from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect
from forms import Person
def signup(request):
# generic view
# 
    if request.method=="POST":
        form==Person(request.POST)
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            return HttpResponse("Your user name must be under 10 characters")
            # messages.error(request, " Your user name must be under 10 characters")
            # return redirect('home')

        if not username.isalnum():
            return HttpResponse(" User name should only contain letters and numbers")
            # messages.error(request, " User name should only contain letters and numbers")
            # return redirect('home')
        if (pass1!= pass2):
            return HttpResponse(" Passwords do not match")
            #  messages.error(request, " Passwords do not match")
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return HttpResponse("Your iCoder has been successfully created")
        # messages.success(request, " Your iCoder has been successfully created")
        # return redirect('home')

    else:
        return render(request, 'base.html')