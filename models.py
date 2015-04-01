from django.db import models

class UserProfile(models.Model):

    # def __init__(self, username, city, items_sold):
    # self.username = username
    # self.city = city
    # self.items_sold = items_sold
    #
    # def personal_profile(object):
    # # set picture, later add interests
    # return
    # def post_item(object):
    # # Picture, price, description, delivery options (in person/mailed)
    # return
    # def messages(object):
    # # actions for sending, receiving, reading messages
    # return
    # def shop_page(object):
    # # set banner, biography/artist statement
    # return
    # def view_history(object):
    # # Keep track of what user has looked at
    # return


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    owner =
    def __str__(self):
        return self.item_text



class Cart(models.Model):
    # def __str__(self):
    # return self.cart_text
    #
    # def add_to_cart(object):
    # # add item logic
    # return
    # def remove_from_cart(object):
    # # remove item logic
    # return
    # def verify_cart(object):
    # # Logic where users have final opportunity to make cart changes
    # return
    # def purchase(object):
    # # Paypal payments go here?
    # return
