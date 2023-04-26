# error classes for order
class CartProductError(Exception):
    code = 400
    message = "This product does not exist in the cart"


class EmptyCartError(Exception):
    code = 400
    message = "Cart is empty"


class EmptyOrderError(Exception):
    code = 400
    message = "No such order exists"
