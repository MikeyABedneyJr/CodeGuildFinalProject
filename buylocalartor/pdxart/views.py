from django.shortcuts import render
from pdxart.models import Product, User, UserProfile


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
        print request.POST
        picture = request.POST['image_upload']
        user = User.objects.create_user(picture)
        user.save()
        profile = UserProfile()
        profile.picture = picture #TODO: Fix profile pic--prob not gonna work
        profile.date = date
        profile.facebook = facebook
        profile.twitter = twitter
        profile.linkedin = linkedin
        profile.address = address #TODO: How to verify address in Oregon?
        profile.bio = bio
        profile.save()
        return redirect('pdxart/index.html')
    return render(request, 'pdxart/registration.html')
