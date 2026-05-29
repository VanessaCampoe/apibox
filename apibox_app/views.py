"""
  HTTP -> Hypertext Transfer Protocol
  HTTPS -> Hypertext Transfer Protocol Secure
  JSON -> JavaScript Object Notation
  https://www.w3schools.com/js/js_json.asp
"""

from django.http import JsonResponse

def box(request):
    if request.method == 'GET':
        box_feira={
            'id': 1,
            'nome': 'Loja Infantil Kids Graça',
            'numero': 101,
        }
        return JsonResponse(box_feira)
