import model


def izpis_igre(igra):
    return (
        f"Igraš igro vislic:\n" +
        f"Narobe ugibane črke so: {igra.nepravilni_ugibi()}\n"+
        f"Trenutno stanje besede: {igra.pravilni_del_gesla()}\n"
    )

def izpis_poraza(igra):
    return (
        f"Izgubil si, več sreče prihodnjič\n"
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n"+
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"+
        f"Pravilno geslo je bilo: {igra.geslo}"
    )

def izpis_zmage(igra):
    return (
        f"Zmagal si, bravo\n"
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n"+
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"+
        f"Pravilno geslo je bilo: {igra.geslo}\n"+
        f"Potreboval si: {len(igra.crke)}." 
    )

def pozeni_vmesnik():
    igra = model.nova_igra(model.bazen_besed)

    while True:
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))
            vnos = input("Vnesi novo črko:")
            igra.ugibaj(vnos)

def pozeni_celotno_igro():    
    while True:
        pozeni_vmesnik()
        if(input("Ali želiš ponovno igrati: Y/N") !="Y"):
            break

pozeni_celotno_igro()

# igra = model.Igra("banana", "")
# print(izpis_igre(igra))
# igra.ugibaj("b")
# print(izpis_igre(igra))
# igra.ugibaj("c")
# print(izpis_igre(igra))
# print(izpis_poraza(igra))