def admin_check(user):
    return user.is_admin


def employee_check(user):
    return user.is_employee or user.is_admin


def customer_check(user):
    return user.is_customer
