class ProductIdError(Exception):
    code = 400
    message = "This product does not exist"
