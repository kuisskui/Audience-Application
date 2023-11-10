from django.http import HttpResponseForbidden

class BlockPathsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_paths = ['/accounts/signup/',
                         '/accounts/inactive/',
                         '/accounts/email/',
                         '/accounts/password/change/',
                         '/accounts/confirm-email/']

        if request.path in blocked_paths:
            return HttpResponseForbidden("Access forbidden to this path.")

        return self.get_response(request)
