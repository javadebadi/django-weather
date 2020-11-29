from django.shortcuts import render

app_name="lookup"
# Create your views here.
def home(request):
    return render(request, "lookup/home.html", {})
