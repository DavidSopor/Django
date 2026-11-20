from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno":"David Sopor",
    }
    return render(request, "cv1/cv1_index.html", kontext)

def cv1_obchod(request):
    produkty = [
        {"nazov": "produkt1", "cena":5.00},
        {"nazov": "produkt2", "cena":4.30},
        {"nazov": "produkt3", "cena":5.680},
        {"nazov": "produkt4", "cena":6.21},
    ]
    e = None
    if request.method == "GET":
        fltr_str = request.GET.get("fltr", "").strip()
        
        if fltr_str:
            try:
                fltr = float(fltr_str)
                prod = []
                for i in produkty:
                    if i["cena"] <= fltr:
                        prod.append(i)
                produkty = prod
            except ValueError:
                e = "nespravny filter"


    return render(request, "cv1/cv1_obchod.html", {"kontext": produkty, "e":e})

def body(request):
    vysledok = None
    z_body = None
    max_body = None
    znamka = None
    if request.method == "POST":
        try:
            z_body = float(request.POST["z_body"])
            max_body = float(request.POST["max_body"])
        except Exception as e:
            return render(request, "cv1/cv1_body.html",{"znamka": "nespravny input"})

        if max_body == 0: return render(request, "cv1/cv1_body.html",{"znamka": "delenie nulou"})

        vysledok = z_body/max_body*100
        if vysledok >= 90: znamka = "1"
        elif vysledok >=75: znamka = "2"
        elif vysledok >=50: znamka = "3"
        elif vysledok >=30: znamka = "4"
        else: znamka = "5"
                

    return render(request, "cv1/cv1_body.html",{"vysledok": vysledok, "z_body": z_body, "max_body": max_body, "znamka": znamka})