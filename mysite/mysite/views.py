from django.shortcuts import redirect

# redirect to main


def redirect_main(request):
    return redirect('main', permanent=True)
