from django.shortcuts import render
from staff import models

def register(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        email = request.POST.get("email",None)
        position = request.POST.get("position",None)
        phoneNumber = request.POST.get("phoneNumber",None)
        salary = request.POST.get("salary",None)
        dateHired = request.POST.get("dateHired",None)

        models.UserInfor.objects.create(    
            nm = name,
            em = email,
            pos = position,
            pn = phoneNumber,
            sl = salary,
            dh = dateHired,
        )

        info_list=models.UserInfor.objects.all()
        return render(request,"employee/index.html",{"info_list":info_list})

    else:
        info_list=models.UserInfor.objects.all()
        return render(request,"employee/index.html",{"info_list":info_list})