def new_password(oldpassword, newpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        return 'True'
    else:
        return 'False'