from django.views import View
from django.http import JsonResponse


class HelloWorldView(View):
    
    def get(self, request):
        print('Hello, World')
        return JsonResponse({'msg': 'hello, world'}, status=200)