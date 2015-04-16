from django.shortcuts import render
from pdxart.models import Product, User, UserProfile
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    # Query the database for a list of ALL products currently stored.
    # Order the products by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Product.objects.order_by('-likes')[:5]
    context_dict = {'products': category_list}

    # Render the response and send it back!
    return render(request, 'pdxart/index.html', context_dict)


def registration(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # picture = request.POST['image_upload']
        user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
        user.save()
        profile = UserProfile()
        u = User.objects.get(username=username)
        profile.user = u
        # profile.picture = picture #TODO: Fix profile pic--prob not gonna work
        profile.date = request.POST['dob']
        profile.website = request.POST['website']
        profile.facebook = request.POST['facebook']
        profile.twitter = request.POST['twitter']
        profile.linkedin = request.POST['linkedin']
        # profile.address = request.POST['address']
            # TODO: How to verify address in Oregon?
            # TODO: Add gender
        profile.bio = request.POST['bio']
        profile.save()
        return HttpResponseRedirect('/pdxart/index/')
    return render(request, 'pdxart/registration.html')
