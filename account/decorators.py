from django.http import HttpResponse
from django.shortcuts import redirect
 
 
def admin_only(view_func):
   def wrapper_func(request, *args, **kwargs):
       if request.user.is_superuser:
           return view_func(request, *args, **kwargs)
       else:
           return redirect('account:login')
 
   return wrapper_func
