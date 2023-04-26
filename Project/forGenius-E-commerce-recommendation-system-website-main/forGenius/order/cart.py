from order.models import Order, Cart
from order.errors import CartProductError, EmptyCartError
from product.models import Product
from product.errors import ProductIdError
from user.models import User
from user.errors import InputError

# the function to add product item to cart
def add_to_cart(email, product_id, quantity):
    # if the user does not exist, raise error
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # if the product does not exist, raise error
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    try:
        # if the product is in the cart, 
        # add the new quantity amount to the original quantity in database
        
        user_cart = Cart.objects.get(
            user_email=user_email, product_id=product_id)
        user_cart.quantity = quantity + user_cart.quantity
        user_cart.save()
        
    except Cart.DoesNotExist:
        # if the product is not in the cart, add the product to cart with the quantity provided
        
        to_cart = Cart(user_email=user_email,
                       product_id=product_id, quantity=quantity)
        to_cart.save()


# the function to view the user's cart
def view_cart(email):
    # if the user does not exist, raise error
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # get the user's cart data
    cart = Cart.objects.filter(user_email=user_email)
    data = {
        "cart": [],
        "total": 0
    }
    total = 0

    # put the data from database to data
    for item in cart:
        info = {
            "product_id": item.product_id.product_id,
            "name": item.product_id.name,
            "price": item.product_id.price,
            "quantity": item.quantity,
            "picture": item.product_id.picture,
            "total_price": item.quantity * item.product_id.price
        }
        total += item.quantity * item.product_id.price
        data["cart"].append(info)

    data["total"] = total
    return data

# the function to edit the product's quantity in the cart
def edit_cart_product_quantity(email, product_id, quantity):
    # if the user does not exist, raise error
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # if the product does not exist, raise error
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    # if the product is in the cart, change the product's quantity
    # if not, raise error
    try:
        user_cart = Cart.objects.get(
            user_email=user_email, product_id=product_id)
        user_cart.quantity = quantity
        user_cart.save()
    except Cart.DoesNotExist:
        raise CartProductError("This product does not exist in the cart")

# the function to remove the product in cart
def remove_cart_product(email, product_id):
    # if the user does not exist, raise error
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # if the product does not exist, raise error
    try:
        product_id = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    # if the product is in the cart, delete the product from the cart
    # if not, raise error
    try:
        user_cart = Cart.objects.get(
            user_email=user_email, product_id=product_id)
        user_cart.delete()
    except Cart.DoesNotExist:
        raise CartProductError("This product does not exist in the cart")
