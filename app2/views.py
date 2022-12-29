from django.shortcuts import render
# write your view here
def jinja_temp(request):
    d={'name':'Shubham','Education':'B.tech(cse)','year':2022}
    return render(request,'jinja_temp.html',d)