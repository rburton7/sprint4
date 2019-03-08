from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>")

    if request.method == "POST":
        print( request.POST.get('yourname'))
        print( request.POST.get('youremail'))
        print( request.POST.get('happy'))
    
    context = {

    }

    return request.dmp.render('contact.html',context)

