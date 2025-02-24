# Descrizione progetto
## Il programma consenta la gestione delle prenotazioni di un ristorante. Il sistema prevede:
 - L’aggiunta di una nuova prenotazione, con il nome del cliente, il numero di persone e l’orario della prenotazione.
 - La visualizzazione dell’elenco delle prenotazioni per una data specifica.
 - La possibilità di modificare un’orario di prenotazione già registrato.
 - L’eliminazione di una prenotazione su richiesta del cliente.

# Funzionalità Aggiunte

## Luca Di Giacomo
- **Funzione:** aggiunta prenotazione
- **Dettaglio:** aggiunta la funzione dell'aggiunta di una nuova prenotazione e per ogni prenotazione aggiunta avviene la stampa.

       def aggiungi_prenotazione(prenotazione, id, nome, numero_persone, data, ora):
        
        id = prenotazione[-1]["id"] + 1
        pren = {"id":id, "nome":nome, "num_per":numero_persone, "data":data, "ora":ora}
        prenotazione.append(pren)
        
        print(f"\n{nome} ha prenotato per {numero_persone} persone il giorno {data} alle ore {ora}\n")
        
        for pren in prenotazione:
            print(pren, "\n")
        return prenotazione

## Matteo Liberati
- **Funzione:** visualizza prenotazione
- **Dettaglio:** aggiunta la funzione di visualizzazione della prenotazione in base alla data e inserendola viene effettuata la stampa per ogni prenotazione in base ad essa.

        def visualizza_prenotazioni(prenotazione, data):
        
        for pren in prenotazione:
            
            if pren["data"] == data:
                print(f"\n{pren['nome']} ha prenotato per {pren['num_per']} persone il giorno {pren['data']} alle ore {pren['ora']}\n")
        else:
            print("\nNessuna prenotazione trovata\n")

## Andrea Luminari
- **Funzione:** modifica orario
- **Dettaglio:** aggiunta la funzione della modifica di un orario già registrato, inserendo l'id della prenotazione, viene richiamato il documento associato ad esso e inserendo un nuovo orario viene eseguita la modifica del documento. Se l'ID non è associato a nessuna prenotazione, viene eseguita una stampa dell'id non valido.

        def modifica_orario(prenotazione, id_pren, ora):
        
        for pren in prenotazione:
            
            if id_pren == pren["id"]:
                pren["ora"] = ora
                print(f"La prenotazione di {pren['nome']} nell'indice {pren['id']}, è stata modificata alle ore {ora}")
                
                for pren in prenotazione:
                    print(pren, "\n")
                return prenotazione
            else:
                print("ID non valido")
                return prenotazione

## Andrea Vizzarri
- **Funzione:** elimina prenotazione
- **Dettaglio:** aggiunta la funzione che elimina una prenotazione. Inserendo l'id della prenotazione viene rimosso il documento da esso associato. Se l'ID non è associato a nessuna prenotazione, viene eseguita una stampa dell'id non valido.

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
