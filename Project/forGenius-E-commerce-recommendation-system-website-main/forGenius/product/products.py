from product.models import Product, Features
from product.errors import ProductIdError
from user.models import Admin
from datetime import datetime, timedelta

ADMIN_EMAIL = '3900forgenius@gmail.com'

# get the Admin information
def get_Admin():
    return Admin.objects.get()

# return particular the product information by product id
def product_userView(product_id):
    try:
        product_query = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")

    # update the delivery date
    delivery_date = datetime.now() + timedelta(days=product_query.delivery_date)

    # input the product information
    info = {
        "name": product_query.name,
        "description": product_query.description,
        "warranty": product_query.warranty,
        "delivery_date": delivery_date.strftime("%Y-%m-%d"),
        "price": round(float(product_query.price), 2),
        "picture": product_query.picture,
        "features": get_product_features(product_id)
    }
    # return the product
    return info


# add new product in the database
def admin_add_product(name, description, warranty, delivery_date, price, picture, features):
    if picture == "":
        picture = "https://i.imgur.com/cscnobv.png"
    # create new product information
    reg = Product(admin_email=get_Admin(), name=name, description=description,
                  warranty=warranty, delivery_date=delivery_date, price=price, picture=picture)
    # save the information in the database
    reg.save()

    # save the feature of the product
    for feature in features.split():
        fe = Features(product_id=reg, feature=feature.capitalize())
        fe.save()

# edit one product in the database
def admin_edit_product(product_id, name, description, warranty, delivery_date, price, picture, features):
    # output the product in the database
    try:
        reg = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")
    reg.name = name
    reg.description = description
    reg.warranty = warranty
    reg.delivery_date = delivery_date
    reg.price = price
    reg.picture = picture

    # update the product with new information
    reg.save()
    # delete old features
    for fe in Features.objects.filter(product_id=product_id):
        fe.delete()
    # add new features
    for feature in features.split():
        fe = Features(product_id=reg, feature=feature)
        fe.save()

# delete one product in the database
def admin_delete_product(product_id):
    # search the product in the database
    try:
        reg = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        raise ProductIdError("This product does not exist")
    # delete the relevant features
    for fe in Features.objects.filter(product_id=product_id):
        fe.delete()
    # delete the product
    reg.delete()

# return all the product infomration
def admin_products_all():
    try:
        books = Product.objects.all()
    except:
        pass
    info_str = "product_details"
    data = {info_str: []}
    # output the information of each product
    for book in books:
        info = {
            "product_id": book.product_id,
            "name": book.name,
            "warranty": book.warranty,
            "description": book.description,
            "delivery_date": book.delivery_date,
            "sales_data": book.sales_data,
            "price": round(float(book.price), 2),
            "picture": book.picture,
            "features": get_product_features(book.product_id)
        }
        data[info_str].append(info)
    return data

# return all the product infomration in sales data order
def admin_products_all_sort(sorting):
    data = admin_products_all()
    
    # check the sorting is valid or not, if not valid,just return answer from admin_products_all()
    if (sorting != "high_to_low" and sorting != "low_to_high"):
        return data
    
    # if it is valid, return list in order
    info_str = "product_details"
    
    # sort the list in sales data order
    result_list = sort_help(sorting, data[info_str])
    res = {info_str: []}
    res[info_str] = result_list
    return res

# the helper function for sorting
def sort_help(sorting, list):
    result = []
    return recursion_help(result, list, sorting)

# the helper function for recursion sort list in sales data order   
def recursion_help(result, list, sorting):
    if len(list) == 0:
        return result
    first = 0
    # choose the chosen method based on the sorting
    for j in range(0, len(list)):
        if (sorting == "high_to_low"):
            if list[j]["sales_data"] > list[first]["sales_data"]:
                first = j
        if (sorting == "low_to_high"):
            if list[j]["sales_data"] < list[first]["sales_data"]:
                first = j

    # add the most optinal one in the result lists and start next recursion.
    result.append(list[first])
    list.remove(list[first])
    return recursion_help(result, list, sorting)


# get the features of one product
def get_product_features(product_id):
    arr = []
    # add the relevant features in the array
    for fe in Features.objects.filter(product_id=product_id):
        arr.append(fe.feature.capitalize())
    return ' '.join(arr)
