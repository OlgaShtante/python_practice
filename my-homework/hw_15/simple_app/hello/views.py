from django.http import HttpResponse

def hello_view(request):
    name = request.GET.get('name', 'World')
    message = request.GET.get('message', 'Have a nice day')
    greeting = f'Hello, {name}! {message}'
    return HttpResponse(greeting)