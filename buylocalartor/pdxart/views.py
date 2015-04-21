from django.shortcuts import render
from pdxart.models import Product, User, UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
