from django.shortcuts import render, HttpResponse

def domace(request):
    text = "Moje domace ulohy"
    return render(request, "domace/domace.html", {"text": text})