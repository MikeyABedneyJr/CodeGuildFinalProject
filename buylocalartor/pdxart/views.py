from django.shortcuts import render
from pdxart.models import Product, User, UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    # Query the database for a list of ALL products currently stored.
    # Order the products by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Product.objects.order_by('-likes')[:5]
    context_dict = {'products': category_list}

    # Render the response and send it back!
    return render(request, 'pdxart/index.html', context_dict)


# Initial log in page --------------------------------------------------------------------------------------------------------------------
def registration(request):
    if request.POST:
        email = request.POST['email']
        username = request.POST['email'] # Only logging in /w email
        password = request.POST['password']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        # picture = request.POST['image_upload']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        profile = UserProfile()
        u = User.objects.get(username=username)
        profile.user = u
        # profile.picture = picture #TODO: Fix profile pic--prob not gonna work
        # profile.date = request.POST['dob']
            # TODO: How to verify address in Oregon?
        profile.save()
        return HttpResponseRedirect('/pdxart/index/')
    return render(request, 'pdxart/registration.html')


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/pdxart/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account has been disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'pdxart/login.html', {})


# Logging out --------------------------------------------------------------------------------------------------------------------

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/pdxart/')

# Stored profile --------------------------------------------------------------------------------------------------------------------
@login_required
def profile(request):
    p = UserProfile.objects.get(user = request.user)
    context_dict = {'profile': p}
    return render(request, 'pdxart/profile.html', context_dict)



# Updating log in page --------------------------------------------------------------------------------------------------------------------
@login_required
def update_profile(request):
    user = User.objects.get(username=request.user)
    profile = UserProfile.objects.filter(user=request.user)[0]
    if request.POST:
        user.email = request.POST.get('email')
        user.firstname = request.POST.get('firstname')
        user.lastname = request.POST.get('lastname')
        user.save()

        profile.address = request.POST['address']
        profile.linkedin = request.POST.get('linkedin')
        profile.twitter = request.POST.get('twitter')
        profile.facebook = request.POST.get('facebook')
        # profile.date = request.POST['dob']
        profile.bio = request.POST.get('bio')
        profile.save()

        return HttpResponseRedirect('/pdxart/index/')

    return render(request, 'pdxart/updateprofile.html', {'email': user, 'profile': profile})
