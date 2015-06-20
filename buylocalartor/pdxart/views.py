from django.shortcuts import render
from pdxart.models import Product, User, UserProfile, Medium
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Main landing page ----------------------------------------------------------------------------------------------------
def index(request):
    # Query the database for a list of ALL products currently stored.
    # Order the products by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Product.objects.order_by('-likes')[:5]
    context_dict = {'products': category_list}

    return render(request, 'pdxart/index.html', context_dict)

# Upgrading landing page ---------------------------------------------------------------------------------------------
def index_new(request):
    return render(request, 'pdxart/index_new.html')

# Initial registration page --------------------------------------------------------------------------------------------
def registration(request):
    if request.POST:
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        profile = UserProfile()
        profile.user = user
        try:
            profile.picture = request.FILES['image_upload']
        except:
            pass
        profile.dob = request.POST['dob']
        # TODO: How to verify address in Oregon?
        profile.save()
        return HttpResponseRedirect('/pdxart/')

    return render(request, 'pdxart/registration.html')


# Quick log in ---------------------------------------------------------------------------------------------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/pdxart/')
            else:
                return HttpResponse("Your account has been disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'pdxart/login.html', {})


# Logging out ----------------------------------------------------------------------------------------------------------
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/pdxart/')


# Stored profile -------------------------------------------------------------------------------------------------------
@login_required
def profile(request):
    p = UserProfile.objects.get(user=request.user)
    context_dict = {'profile': p}
    return render(request, 'pdxart/profile.html', context_dict)


# Updating log in page -------------------------------------------------------------------------------------------------
@login_required
def update_profile(request):
    profile = UserProfile.objects.filter(user=request.user)[0]
    if request.POST:
        profile = UserProfile()
        profile.user = request.user
        profile.email = request.POST['email']
        profile.firstname = request.POST['firstname']
        profile.lastname = request.POST['lastname']
        profile.address = request.POST['address']
        profile.linkedin = request.POST['linkedin']
        profile.twitter = request.POST['twitter']
        profile.facebook = request.POST['facebook']
        profile.dob = request.POST['dob']
        profile.bio = request.POST['bio']
        profile.save()
        return HttpResponseRedirect('/pdxart/')
    return render(request, 'pdxart/updateprofile.html', {'email': request.user, "profile": profile})


# Viewing personal inventory page --------------------------------------------------------------------------------------
@login_required
def inventory(request):
    # Create a context dictionary which we can pass to the template rendering engine.
    products = Product.objects.all()
    context_dict = {'products': products}
    # Go render the response and return it to the client.
    return render(request, 'pdxart/inventory.html', context_dict)


# WHen you want to add a new item to your inventory---------------------------------------------------------------------
@login_required
def addinventory(request):
    media_list = Medium.objects.all()
    media = []
    for i in media_list:
        media.append({'name': i.material})
    context_dict = {'media': media}
    if request.POST:
        product = Product()
        product.owner = request.user
        product.name = request.POST['itemname']
        product.price = request.POST['price']
        product.medium = Medium.objects.get(material=request.POST['medium'])
        product.description = request.POST['description']
        product.picture = request.FILES['item_image_upload']
        product.save()
        return HttpResponseRedirect('/pdxart/')
    return render(request, 'pdxart/addinventory.html', context_dict)
