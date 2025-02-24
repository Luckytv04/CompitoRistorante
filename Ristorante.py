class Prenotazione:
    
    prenotazione = [{"id":1,"nome":"Pasquino", "num_per":4, "data":"12/12/2021", "ora":"13:00"},
                    {"id":2, "nome":"Graziella", "num_per":2, "data":"12/12/2021", "ora":"21:00"},
                    {"id":3, "nome":"Robbino", "num_per":1, "data":"12/12/2021", "ora":"22:00"},
                    {"id":4, "nome":"Pasquino", "num_per":4, "data":"20/02/2021", "ora":"14:30"},
                    ]
        
    def aggiungi_prenotazione(prenotazione, id, nome, numero_persone, data, ora):
        
        id = prenotazione[-1]["id"] + 1
        pren = {"id":id, "nome":nome, "num_per":numero_persone, "data":data, "ora":ora}
        prenotazione.append(pren)
        
        print(f"{nome} ha prenotato per {numero_persone} persone il giorno {data} alle ore {ora}")
        
        for pren in prenotazione:
            print(pren, "\n")
        return prenotazione
    
    def visualizza_prenotazioni(prenotazione, data):
        
        for pren in prenotazione:
            
            if pren["data"] == data:
                print(f"\n{pren['nome']} ha prenotato per {pren['num_per']} persone il giorno {pren['data']} alle ore {pren['ora']}\n")
                
                
    def modifica_orario(prenotazione, id_pren, ora):
        
        for pren in prenotazione:
            
            if id_pren == pren["id"]:
                pren["ora"] = ora
                print(f"\nLa prenotazione di {pren['nome']} nell'indice {pren['id']}, è stata modificata alle ore {ora}\n")
                
                for pren in prenotazione:
                    print(pren, "\n")
                return prenotazione
            else:
                print("ID non valido")
                return prenotazione
        
    def elimina_pren(prenotazione, id):
        
        for pren in prenotazione:
            
            if pren["id"] == id:
                
                prenotazione.remove(pren)
                print(f"\nLa prenotazione con indice {id} è stata eliminata\n")
                
                for pren in prenotazione:
                    print(pren, "\n")
                return prenotazione
            
            else:
                print("ID non valido")
                return prenotazione
            
class GestionePren:
                
    a = Prenotazione.prenotazione
    b = Prenotazione.aggiungi_prenotazione
    c = Prenotazione.visualizza_prenotazioni
    d = Prenotazione.modifica_orario
    e = Prenotazione.elimina_pren

    scelta = 0

    while(scelta != 5):
    
        scelta = int(input("1. Aggiungi prenotazione\n2. Visualizza prenotazioni\n3. Modifica ora prenotazione\n4. Elimina prenotazione \n5. Esci \n \n"))

        match scelta:
        
            case 1:
                b(a, id, input("Nome: "), input("Numero di persone: "), input("Data: "), input("Ora: "))
        
            case 2:
                c(a, input("Immettere la data di prenotazione: "))
            
            case 3:
                d(a, int(input("ID prenotazione: ")), input("Nuovo orario: "))
            
            case 4:
                e(a, int(input("ID prenotazione da eliminare: ")))
            
            case 5:
                break
        
            case _:
                print("Scelta non valida")
                break