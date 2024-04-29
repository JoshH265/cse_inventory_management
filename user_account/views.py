from django.shortcuts import render

def user_account(request):
    return render(request, 'user_account/userprofile.html')
