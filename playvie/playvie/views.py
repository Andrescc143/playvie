from django.http import JsonResponse


def handler404(request, exception=None):
    return JsonResponse({'error': 'Resource Not Found (404)'}, status=404)