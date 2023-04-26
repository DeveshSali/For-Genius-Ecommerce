from user.models import Address_book, User
from user.auth import InputError


def view_address_book(email):
    """
    view_address_book(email)
    view address book according to email
    """
    # search address book database
    try:
        books = Address_book.objects.filter(user_email=email)
    except:
        pass

    # initialize address book data
    data = {"address_book": []}

    # add search results one by one to address book data
    for book in books:
        info = {
            "address_id": book.address_id,
            "name": book.name,
            "address_line": book.address_line,
            "post_code": book.post_code,
            "suburb": book.suburb,
            "state": book.state,
            "country": book.country,
            "phone_number": book.phone_number
        }
        data["address_book"].append(info)

    # return address book data
    return data


def delete_address_book(email, address_id):
    """
    delete_address_book(email, address_id)
    delete specific address in the address book
    email for checking user authorization (potential attack: one user delete another user's address)
    """
    # check if specific address exists
    try:
        address = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('Address ID not exist')

    # delete specific address
    address.delete()


def edit_address_book(email, name, address_line, post_code, suburb, state, country, phone_number, address_id):
    """
    edit_address_book(email, name, address_line, post_code, suburb, state, country, phone_number, address_id)
    edit specific address in the address book
    email for checking user authorization (potential attack: one user edit another user's address)
    """
    # check if specific address exists
    try:
        info = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('Address book exist')

    # edit and save specific address
    info.name = name
    info.address_line = address_line
    info.post_code = post_code
    info.suburb = suburb
    info.state = state
    info.country = country
    info.phone_number = phone_number
    info.save()


def add_address_book(email, name, address_line, post_code, suburb, state, country, phone_number):
    """
    add_address_book(email, name, address_line, post_code, suburb, state, country, phone_number)
    add new address to the address book
    """
    # check if user email exists
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # create and save new address
    reg = Address_book(user_email=user_email, name=name, address_line=address_line,
                       post_code=post_code, suburb=suburb, state=state, country=country,
                       phone_number=phone_number)
    reg.save()


def address_book_detail(token, email, address_id):
    """
    address_book_detail(token, email, address_id)
    view specific address in the address book
    """
    # check if specific address exists
    try:
        info = Address_book.objects.get(address_id=address_id)
    except Address_book.DoesNotExist:
        raise InputError('User not exist')

    # create specific address data
    data = {
        "token": token,
        "address": info.address,
        "name": info.name,
        "address_line": info.address_line,
        "post_code": info.post_code,
        "suburb": info.suburb,
        "state": info.state,
        "country": info.country,
        "phone_number": info.phone_number,
        "address_id": info.address_id,
    }

    # return specific address data
    return data
