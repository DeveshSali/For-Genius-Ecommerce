from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.http.response import JsonResponse
from product.errors import ProductIdError
from product.models import Features
from user.auth import token_to_email
from user.errors import InputError
import product.products as products
import product.recommendation as recommendation
import product.search as search_result
import user.auth as auth
import jwt as jwt
import json

# Create your views here.

# check if the str can be converted to float
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# request for viewing the product
def view_product_user(request):

    response = HttpResponse()
    if request.method == "GET":

        product_id = request.GET.get("product_id")

        if product_id is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        try:
            data = products.product_userView(product_id)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        meta = {'msg': 'OK', 'status': 200}
        jsons = {
            'data': data,
            'meta': meta
        }
        return JsonResponse(jsons)
    response.status_code = 405
    return response


# request for adding new product
def admin_add_product(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            name = data['name']
            description = data['description']
            warranty = data['warranty']
            delivery_date = data['delivery_date']
            price = data['price']
            picture = data['picture']
            features = data['features']
            if not isFloat(price) or float(price) <= 0:
                response.status_code = 443
                response.content = 'price is not float'
                return response
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_add_product(
                name, description, warranty, delivery_date, price, picture, features)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response


# request for editing the chosen product
def admin_edit_product(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            name = data['name']
            description = data['description']
            warranty = data['warranty']
            delivery_date = data['delivery_date']
            price = data['price']
            product_id = data['product_id']
            picture = data['picture']
            features = data['features']
            if not isFloat(price) or float(price) <= 0:
                response.status_code = 443
                response.content = 'price is not float or price <= 0'
                return response
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_edit_product(
                product_id, name, description, warranty, delivery_date, price, picture, features)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response

# request for deleting the chosen product
def admin_delete_product(request):
    response = HttpResponse()
    if request.method == "DELETE":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            #token = data["token"]
            #email = auth.token_to_email(token)
            product_id = data['product_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            products.admin_delete_product(product_id)
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return response
    response.status_code = 405
    return response


# request for the recommendation list for guests
def admin_products_all(request):
    response = HttpResponse()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response
        try:
            pass
            #token = data["token"]
            #email = auth.token_to_email(token)
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        try:
            data = products.admin_products_all()
        except ProductIdError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        meta = {'msg': 'OK', 'status': 200}
        jsons = {
            'data': data,
            'meta': meta
        }
        return JsonResponse(jsons)
    response.status_code = 405
    return response

# request for the recommendation list for guests
def admin_products_all_sort(request):
    response = HttpResponse()
    if request.method == "GET":
        sorting = request.GET.get("sorting")
        if sorting is None:
            response.status_code = 442
            response.content = "KeyError"
            return response
        
        try:
            data = products.admin_products_all_sort(sorting)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        meta = {'msg': 'OK', 'status': 200}
        jsons = {
            'data': data,
            'meta': meta
        }
        return JsonResponse(jsons)
    response.status_code = 405
    return response

# request for the recommendation list for guests
def public_recommendation(request):
    
    response = HttpResponse()
    if request.method == "GET":
        try:
            data = recommendation.public_recommendation()
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response


# request for the recommendation list for users
def private_recommendation(request):
    response = HttpResponse()
    if request.method == "GET":
        token = request.GET.get("token")
        email = auth.token_to_email(token)
        try:
            data = recommendation.private_recommendation(email)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response


def get_search_result(request):
    response = HttpResponse()
    if request.method == "GET":
        token = request.GET.get("token")
        if token is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        search = request.GET.get("search")
        if search is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        sorting = request.GET.get("sorting")
        if search is None:
            response.status_code = 442
            response.content = "KeyError"
            return response

        try:
            email = ""
            if token != "":
                email = auth.token_to_email(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response
        except jwt.InvalidSignatureError:
            response.status_code = 400
            response.content = "token is wrong"
            return response

        try:
            data = search_result.get_search_result(email, search, sorting)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")
    response.status_code = 405
    return response
