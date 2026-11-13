from django.shortcuts import render, HttpResponse
from datetime import date
def ahoj(request):
    return HttpResponse("Ahoj svet!")

def o_mne(request):
    kontext = {
        "meno" : "David",
        "vek" : 18,
        "zaluby" : ["skola", "matematika", "hokej"]
    }
    return render(request, "ulohy/o_mne.html", kontext)

def rozvrh(request):
    hodiny = [
        {"cislo" : 1, "predmet" : "Programovanie"},
        {"cislo" : 2, "predmet" : "Programovanie"},
        {"cislo" : 3, "predmet" : "Matematika"},
        {"cislo" : 4, "predmet" : "Prax"},
        {"cislo" : 5, "predmet" : "Prax"},
        {"cislo" : 6, "predmet" : "ANJ"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok", "hodiny": hodiny})

def pozdrav(request):
    meno = request.GET.get("meno", "") # .get najde a vrati hodnotu prvku s indexom (klucom) meno ak nenajde vlozi prazdny string 
    return render(request, "ulohy/pozdrav.html", {"meno":meno})

def sucet(request):
    vysledok = None
    if request.method == "POST":
        a = request.POST["a"]
        b = request.POST["b"]
        vysledok = float(a) + float(b)
    return render(request, "ulohy/sucet.html", {"vysledok": vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        o = request.POST["operacia"]
        if o == "+":
            vysledok = a+b
        elif o == "-":
            vysledok = a-b
        elif o == "*":
            vysledok = a*b
        elif o == "/":
            if b != 0:
                vysledok = a/b
            else:
                vysledok = "delenie nulou"
        
    return render(request, "ulohy/kalkulacka.html", {"vysledok": vysledok})

def obdlznik(request):
    obvod = None
    obsah = None
    if request.method == "POST":
            a = float(request.POST["a"])
            b = float(request.POST["b"])
            obvod = round(2*a+2*b, 2)
            obsah = round(a*b, 2)
    return render(request, "ulohy/obdlznik.html", {"obvod": obvod, "obsah": obsah})

def vek(request):
    zije = None
    if request.method == "POST":
        zije = date.today().year - int(request.POST["rok"])
                
    return render(request, "ulohy/vek.html", {"zije": zije})