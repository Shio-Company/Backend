from django.http import JsonResponse
from django.db import connection

def health_check(request):
    status = {"status": "ok", "database": "disconnected"}
    try:
        connection.ensure_connection()
        status["database"] = "connected"
    except Exception:
        return JsonResponse(status, status=500)
    
    return JsonResponse(status)