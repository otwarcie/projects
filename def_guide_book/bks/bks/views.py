from django.template import Template, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render#, render_to_response
import datetime

def hello(request):
	return HttpResponse('Hello World!')

def goodbye(request):
	return HttpResponse('Goodbye someone.')

def current_datetime(request):
	now = datetime.datetime.now()
	# t = Template("<html><body>It is now {{ current_date}}.</body></html>")
	# html = t.render(Context({'current_date': now}))
	# return HttpResponse(html)
	return render(request, 'current_datetime.html', {'current_date': now})

def request_meta(request):
	values = request.META.items()
	# values.sort()
	# html = []
	req_met = []
	for k,v in values:
		# html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
		req_met.append({k:v})
	# return HttpResponse('<table>%s</table>' % '\n'.join(html))
	return render(request, 'request_meta.html', {'request_meta': req_met, 'title': 'Request META list'})

# def search_form(request):
# 	return render_to_response('search_form.html')
	return render(request, 'search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %s' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)


# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	html = '<html><body>It is now %s.</body></html>' % now
# 	return HttpResponse(html)

def hours_ahead(request, h_ahead):
	try:
		h_ahead = int(h_ahead)
	except ValueError:
		raise Http404()

	now = datetime.datetime.now()
	# assert False
	calculated_time = now + datetime.timedelta(days=h_ahead)
	return render(request, 'hours_ahead.html', {'hour_offset': h_ahead, 'next_time': calculated_time})
	# return HttpResponse('Current time %s plus %d hours is %s' % (now, h_ahead, calculated_time))
