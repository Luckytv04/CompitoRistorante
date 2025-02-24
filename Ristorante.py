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
    
a = Prenotazione.prenotazione
b = Prenotazione.aggiungi_prenotazione

scelta = 0

while(scelta != 5):
    
    scelta = int(input("1. Aggiungi prenotazione\n2. Visualizza prenotazioni\n3. Modifica ora prenotazione\n4. Elimina prenotazione \n5. Esci \n \n"))

    match scelta:
        
        case 1:
            b(a, id, input("Nome: "), input("Numero di persone: "), input("Data: "), input("Ora: "))
            
        
        case _:
            print("Scelta non valida")
            break