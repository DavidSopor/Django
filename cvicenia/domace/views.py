from django.shortcuts import render, HttpResponse

def domace(request):
    text = "Moje domace ulohy"
    return render(request, "domace/domace.html", {"text": text})

def vizitka(request):
    kontext = {
        "meno":"David Sopor",
        "trieda": "3.AT",
        "vek": 18,
        "oblubene_predmety":["TSV","PROG","IOT"],
    }
    return render(request, "domace/du2_.html", kontext)