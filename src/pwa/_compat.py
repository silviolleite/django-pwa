import django

if django.VERSION >= (5, 1):
    from django.contrib.auth.decorators import login_not_required
else:

    def login_not_required(view_func):
        return view_func


__all__ = [
    "login_not_required",
]
