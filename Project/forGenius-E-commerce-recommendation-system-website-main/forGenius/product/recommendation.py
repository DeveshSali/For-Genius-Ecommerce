from product.models import Product, Features
from product.products import get_product_features
from product.search import get_search_result
from user.models import User, Interest, Search_history
from user.errors import InputError
import random


lastDB = {}
# return the recommendation if the user is logout(guest mode)


def public_recommendation():
    products = recomment_by_sales()
    # output the products with ordered number
    products = pick_products(products, 6)
    data = {
        "product_number": len(products),
        "products": products,
    }
    return data

# return the recommendation if the user is logged (user mode)


def private_recommendation(email):
    # search the user email to find its interest
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')
    if email not in lastDB:
        # don't check the repetation
        listA = pick_products(recomment_by_sales(), 2)
        listB = pick_products(recomment_by_interest(email), 4)
        lastDB[email] = combine_list(listA, listB)
    search = pick_products(recomment_by_search(email), 8)
    listC = combine_list(lastDB[email], search)
    lastDB[email] = pick_products(listC, 12)
    # output the products with ordered number
    products = pick_products(lastDB[email], 6)

    data = {
        "product_number": len(products),
        "products": products,
    }
    return data


def recomment_by_sales():
    # sort the product with selling data
    top_selling_products = Product.objects.order_by('-sales_data')
    data = []
    # output the relevant selling products
    for product in top_selling_products:
        info = {
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": round(float(product.price), 2),
            "picture": product.picture,
            "features": get_product_features(product.product_id),
            "sales_data": product.sales_data
        }
        data.append(info)
    return data


def recomment_by_interest(user_email):
    data = []
    # put relevent products with interests in the recommendation array
    interests = Interest.objects.filter(user_email=user_email)
    for interest in interests:
        for feature in Features.objects.filter(feature=interest.interests):
            product = feature.product_id
            info = {
                "product_id": product.product_id,
                "name": product.name,
                "description": product.description,
                "price": round(float(product.price), 2),
                "picture": product.picture,
                "features": get_product_features(product.product_id),
                "sales_data": product.sales_data
            }
            if info not in data:
                data.append(info)
    # sort the products with selling datas
    data = sorted(data, key=lambda x: -x["sales_data"])
    return data


def recomment_by_search(user_email):
    try:
        # get user's search history
        search = Search_history.objects.filter(user_email=user_email)
        
        # get the lastest search of this user
        result = []
        lastest_search = []
        for record in search:
            lastest_search.append(record.search)
        
        # get the product result with the lastest two search history
        # and put them to result list
        for item in get_search_result("", lastest_search[-1], "best_sell"):
            if item not in result:
                result.append(item)

            
        return result
    except:
        return []

# balance recommendation lists to selected number of the products


def balance_products(product_list, num):
    if len(product_list) <= num:
        return product_list
    # use random algorithms to select
    to_delete = random.sample(range(product_list), len(product_list) - num)
    return [x for i, x in enumerate(product_list) if not i in to_delete]

# pick selected number of the products from the recommendation lists


def pick_products(product_list, num):
    if len(product_list) <= num:
        return product_list
    # use random algorithms to select
    samples = random.sample(product_list, num)
    return samples


def combine_list(a_str, b_str):
    id_result = []
    result = []
    for a in a_str:
        if a["product_id"] not in id_result:
            result.append(a)
            id_result.append(a["product_id"])
            
    for b in b_str:
        if b["product_id"] not in id_result:
            result.append(b)
            id_result.append(b["product_id"])
            
    return result
