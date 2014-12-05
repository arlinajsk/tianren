from    django.http import HttpResponse, Http404
from    pytz import timezone
import  datetime

from    django.template.loader  import get_template
from    django.template         import Context
from    django.shortcuts        import render

# takes HttpRequest as its first parameter
# returns HttpResponse
def hello(request):
    return HttpResponse("Hello world")
    
# def home( request ):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse( html )
    
def home( request ):
    now = datetime.datetime.now()
    return render( request, 'current_datetime.html', {'current_date':now} )
    
def hours_ahead( request, offset ):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
