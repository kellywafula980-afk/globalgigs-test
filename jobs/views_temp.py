
def logout_view(request):
    """Logout employer"""
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    from django.contrib import messages
    
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
