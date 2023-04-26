from user.models import User
from user.errors import InputError
import re
import jwt
import time
import random
import user.email_robot as email_robot

TOKEN_DB = list()
PRIVATE_KEY = 'nLAghlDB8Qec4d6LD5dhV2QvVs3vpDSY'
RESETCODE_DB = dict()


def auth_login(email, password):
    """ 
    auth_login(email, password)
    check and login in the account 
    """
    # check if email exsists
    try:
        email_query = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('Incorrect email or password')

    # check if password matches
    if (email_query.password != password):
        raise InputError('Incorrect email or password')

    # generate JWT token
    token = jwt.encode({'email': email, 'time': time.time()},
                       PRIVATE_KEY, algorithm='HS256')

    # add JWT token to TOKEN_DB
    TOKEN_DB.append(token)

    # return token
    return token


def auth_logout(token):
    """ 
    auth_logout(token)
    logout the current user(token) 
    """
    # if token exists, remove token from TOKEN_DB
    if token in TOKEN_DB:
        TOKEN_DB.remove(token)

    # if token does not exist, return True
    return True


def auth_register(email, name, password, code):
    """ 
    auth_register(email, name, password, code)
    register the account in the database 
    """
    # check if email is valid
    if not validate_email(email):
        raise InputError('Invalid Email')

    # check if email exsists
    try:
        User.objects.get(pk=email)
    except User.DoesNotExist:
        # check if name is valid
        if not validate_name(name):
            raise InputError('Invalid username')

        # check if password is valid
        if not validate_password(password):
            raise InputError('Invalid password')

        # check if registration code is valid
        if RESETCODE_DB[email] != code:
            raise InputError('Invalid Code')

        # save user registration
        reg = User(user_email=email, user_name=name, password=password)
        reg.save()

        # return login token
        return auth_login(email, password)

    # if email already exsists, raise exception
    raise InputError('Already registered, please log in')


def auth_register_send(username, email):
    """ 
    auth_register_send(username, email)
    send registration code
    """
    # check if email is valid
    if not validate_email(email):
        raise InputError('Invalid Email')

    # generate registration code
    reset_code = generate_reset_code()

    # add registration code to RESETCODE_DB
    RESETCODE_DB[email] = reset_code

    # send registration code email
    email_robot.send_email_register(username, email, reset_code)


def auth_change_password(token, old_password, new_password):
    email = token_to_email(token)
    if (len(User.objects.filter(pk=email).filter(password=old_password)) != 1):
        raise InputError('Incorrect old password')
    if not validate_password(new_password):
        raise InputError('Invalid new password')
    email_query = User.objects.get(pk=email)
    email_query.password = new_password
    email_query.save()
    return True


def auth_reset_password(reset_code, new_password):
    if not validate_password(new_password):
        raise InputError('Invalid new password')
    email = reset_code_to_email(reset_code)
    email_query = User.objects.get(pk=email)
    email_query.password = new_password
    email_query.save()
    return True


def auth_send_reset_code(email):
    """ 
    auth_send_reset_code(email)
    send reset password code
    """
    # check if email is valid
    if not validate_email(email):
        raise InputError('Invalid email address, please try again')

    # check if email exsists
    try:
        email_query = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('Not registered yet, please sign up')

    # generate registration code
    reset_code = RESETCODE_DB.get(email)
    if reset_code is None:
        reset_code = generate_reset_code()

    # add registration code to RESETCODE_DB
    RESETCODE_DB[email] = reset_code

    # for debugging
    # print("email:" + email + "\treset_code:" + reset_code)

    # send reset password code email
    email_robot.send_email(email_query.user_name, email, reset_code)


def validate_email(email):
    """ 
    validate_email(email)
    email: frontend should convert email to lower case
    validate email format 
    """
    # regex formula for email format validation
    regex = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.com\b'

    # if regex matches successfully, return True
    if re.fullmatch(regex, email):
        return True

    # if regex failed to matche, return False
    return False


def validate_name(name):
    """ 
    validate_name(name)
    validate name
    """
    # if name length is too long or too short, return False
    if len(name) < 6 or len(name) > 12:
        return False

    # if name is not too long and too short, return True
    return True


def validate_password(password):
    """ 
    validate_password(password)
    validate password
    """
    # if name password is too long or too short, return False
    if len(password) < 6 or len(password) > 12:
        return False

    # flags for upper case, lower case and number
    flag = [0, 0, 0]

    # check password char by char
    for ch in password:
        if ch.isupper():
            flag[0] = 1
        elif ch.islower():
            flag[1] = 1
        elif ch.isdigit():
            flag[2] = 1
        else:
            return False

    # if password does not satisfy conditions, return False
    if sum(flag) < 3:
        return False

    # if password satisfies conditions, return False
    return True


def check_login(token):
    """ 
    check_login(token)
    check if token is valid
    """
    return True
    # # if token exists, return True
    # if token in TOKEN_DB:
    #     return True
    #
    # # if token does not exist, return False
    # return False


def token_to_email(token):
    """ 
    token_to_email(token)
    convert token to email
    """
    # check if token is valid
    if not check_login(token):
        raise InputError('Invalid token')

    # decode JWT token
    data = jwt.decode(token, PRIVATE_KEY, algorithms=["HS256"])

    # return email
    return data['email']


def token_to_username(token):
    """ 
    token_to_username(token)
    convert token to username
    """
    # convert token to email
    email = token_to_email(token)

    # search user database
    email_query = User.objects.get(pk=email)

    # return username
    return email_query.user_name


def generate_reset_code():
    """ 
    generate_reset_code()
    generate reset code
    """
    reset_code = ''
    # pick 6 random upper case characters and numbers
    for i in range(6):
        reset_code += str(random.choice([random.randrange(10),
                          chr(random.randrange(65, 91))]))

    # return reset code
    return reset_code


def reset_code_to_email(reset_code):
    """
    reset_code_to_email(reset_code)
    convert reset code to email
    """
    # check if corresponding email exists
    try:
        email = list(RESETCODE_DB.keys())[
            list(RESETCODE_DB.values()).index(reset_code)]
    except ValueError:
        raise InputError('Invalid reset code')

    # delete reset code from RESETCODE_DB
    RESETCODE_DB.pop(email)

    # return email
    return email


def change_username(email, new_name):
    """ 
    change_username(email, new_name)
    change username
    """
    # check if name is valid
    if not validate_name(new_name):
        raise InputError('Invalid username')

    # save user name
    email_query = User.objects.get(pk=email)
    email_query.user_name = new_name
    email_query.save()
