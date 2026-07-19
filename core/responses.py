from django.http import JsonResponse


def api_response(data=None, message="", status=200, success=None):
    if success is None:
        success = status < 400
    return JsonResponse(
        {
            "success": success,
            "status": status,
            "message": message,
            "data": data,
        },
        status=status,
    )