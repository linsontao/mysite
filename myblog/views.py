from django.shortcuts import render
from myblog import models
# Create your views here.

def get_db():
    user_list = models.UserInfo.objects.all()
    for user in user_list:
        print(user.user, user.pwd)



def index(request):
    user_list = models.UserInfo.objects.all()
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        # models.UserInfo.objects.create(user=username, pwd=password)
        user_obj = models.UserInfo.objects.filter(user=username)
        if user_obj and user_obj[0] in user_list:
            models.UserInfo.objects.update_or_create(user=username, defaults={"user":username, 'pwd':password})
        else:
            models.UserInfo.objects.create(user=username,pwd=password)
    user_list1 = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list1})
