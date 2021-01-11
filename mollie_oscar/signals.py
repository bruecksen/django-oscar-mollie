import django.dispatch

payment_successfull = django.dispatch.Signal(providing_args=["order", "payment_id"])