from django.http import HttpResponse, JsonResponse

def home_page(request):
    print('HonmePage')
    friends = ['anki', 'amir', 'roshith']
    return JsonResponse(friends, safe=False)