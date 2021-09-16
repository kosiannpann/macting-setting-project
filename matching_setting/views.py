from django.shortcuts import render

# Create your views here.


def matching_setting_list(request):
    return render(request, 'matching_setting/matching_setting_list.html', {})
