from user.models import User, Interest
from user.errors import InputError


def user_interest(email, interest_list):
    '''
    set user interest
    '''
    # check if user exsists
    try:
        user_email = User.objects.get(pk=email)
    except User.DoesNotExist:
        raise InputError('User not exist')

    # save user interests
    for interest in interest_list:
        try:
            Interest.objects.get(user_email=user_email, interests=interest)
        except Interest.DoesNotExist:
            interest_save = Interest(user_email=user_email, interests=interest)
            interest_save.save()
