from django.http.response import JsonResponse
from django.http import HttpResponse
from user.errors import InputError
import json
import user.auth as auth
import user.address as address
import user.interest as interest
import jwt as jwt

ADMIN_EMAIL = '3900forgenius@gmail.com'

# Create your views here.


def register_send(request):
    """
    url: http://127.0.0.1:8000/user/register/send_code
    method: POST
    """
    response = HttpResponse()
    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            email = data["email"]
            name = data["name"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            auth.auth_register_send(name, email)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def register(request):
    """
    url: http://127.0.0.1:8000/user/register/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            email = data["email"]
            name = data["name"]
            password = data["password"]
            code = data["code"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            token = auth.auth_register(email, name, password, code)
            username = auth.token_to_username(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        data = {
            'token': token,
            'username': username,
        }

        return HttpResponse(json.dumps(data), content_type="application/json")

    response.status_code = 405
    return response


def login(request):
    """
    url: http://127.0.0.1:8000/user/login/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            token = auth.auth_login(email, password)
            username = auth.token_to_username(token)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        data = {
            'token': token,
            'username': username,
        }

        if email == ADMIN_EMAIL:
            return HttpResponse(json.dumps(data), content_type="application/json", status=255)

        return HttpResponse(json.dumps(data), content_type="application/json")

    response.status_code = 405
    return response


def logout(request):
    """
    url: http://127.0.0.1:8000/user/logout/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        auth.auth_logout(token)
        response.status_code = 200
        return response

    response.status_code = 405
    return response


def change_password(request):
    """
    url: http://127.0.0.1:8000/user/change_password/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            old_password = data["old_password"]
            new_password = data["new_password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            auth.auth_change_password(token, old_password, new_password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def send_reset_code(request):
    """
    url: http://127.0.0.1:8000/user/send_reset_code/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            email = data["email"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            auth.auth_send_reset_code(email)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def reset_password(request):
    """
    url: http://127.0.0.1:8000/user/reset_password/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            reset_code = data["reset_code"]
            new_password = data["new_password"]
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
            auth.auth_reset_password(reset_code, new_password)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def add_address_book(request):
    """
    url: http://127.0.0.1:8000/user/address/add/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            email = auth.token_to_email(token)
            name = data['name']
            address_line = data['address_line']
            post_code = data['post_code']
            suburb = data['suburb']
            state = data['state']
            country = data['country']
            phone_number = data['phone_number']
            if not str.isdigit(phone_number):
                response.status_code = 443
                response.content = 'Phone Number is not digitial'
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
            address.add_address_book(
                email, name, address_line, post_code, suburb, state, country, phone_number)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def view_address_book(request):
    """
    url: http://127.0.0.1:8000/user/address/view/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            email = auth.token_to_email(token)
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        try:
            data = address.view_address_book(email)
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


def delete_address_book(request):
    """
    url: http://127.0.0.1:8000/user/address/delete/
    method: DELETE
    """
    response = HttpResponse()

    if request.method == "DELETE":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            email = auth.token_to_email(token)
            address_id = data['address_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        try:
            address.delete_address_book(email, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def edit_address_book(request):
    """
    url: http://127.0.0.1:8000/user/address/edit/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            email = auth.token_to_email(token)
            name = data['name']
            address_line = data['address_line']
            post_code = data['post_code']
            suburb = data['suburb']
            state = data['state']
            country = data['country']
            phone_number = data['phone_number']
            address_id = data['address_id']
            if not str.isdigit(phone_number):
                response.status_code = 443
                response.content = 'Phone Number is not digitial'
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
            data = address.edit_address_book(
                email, name, address_line, post_code, suburb, state, country, phone_number, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")

    response.status_code = 405
    return response


def address_book_detail(request):
    """
    url: http://127.0.0.1:8000/user/address/detail/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            email = auth.token_to_email(token)
            address_id = data['address_id']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        try:
            data = address.address_book_detail(token, email, address_id)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return HttpResponse(json.dumps(data), content_type="application/json")

    response.status_code = 405
    return response


def add_user_interests(request):
    """
    url: http://127.0.0.1:8000/user/address/detail/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            interest_list = data['interest']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
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
            interest.user_interest(email, interest_list)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response


def change_username(request):
    """
    url: http://127.0.0.1:8000/user/change_username/
    method: POST
    """
    response = HttpResponse()

    if request.method == "POST":

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response.status_code = 441
            response.content = 'json.JSONDecodeError'
            return response

        try:
            token = data["token"]
            new_name = data['newname']
        except KeyError:
            response.status_code = 442
            response.content = 'KeyError'
            return response

        try:
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
            auth.change_username(email, new_name)
        except InputError as e:
            response.status_code = 400
            response.content = e
            return response

        response.status_code = 200
        return response

    response.status_code = 405
    return response
