from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Allow both GET and POST methods for logout
        if request.method == 'GET' or request.method == 'POST':
            return super().dispatch(request, *args, **kwargs)
        return self.http_method_not_allowed(request, *args, **kwargs)
