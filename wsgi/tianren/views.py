import os
from django.shortcuts import render_to_response, render
import datetime
def home(request):
    now = datetime.datetime.now()
    return render( request, 'home/home.html', {'current_date':now} )
    #return render_to_response('home/home.html')

