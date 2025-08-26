from typing import Dict
from utils.ticket import Ticket


TICKET_DATASET: Dict[int, Ticket] = {
    1: Ticket(
        id="TKT-001",
        subject="Email Signatur lädt nicht",
        body="""Ich habe jeden Tag Probleme mit meiner E-Mail Signatur. Sie lädt nicht richtig.
        "Das Problem tritt täglich mehrmals auf und ich muss jedes mal händisch die Signatur anpassen!
        "Es kostet mich viel Zeit und Nerven. Bitte um schnelle Hilfe!""",
    ),
    2: Ticket(
        id="TKT-002",
        subject="OneDrive Sync Problem",
        body="""Guten Tag, beim Öffnen einer Datei im Explorer erhalte ich die Meldung, 
        dass die Datei nicht gefunden wurde, obwohl sie in OneDrive vorhanden ist.""",
    ),
    3: Ticket(
        id="TKT-003",
        subject="PDFXChange installieren",
        body="""Hallo, ich brauche den PDFXChange auf meinem Laptop. 
        Könnt ihr mir diesen bitte installieren.""",
    ),
    4: Ticket(
        id="TKT-004",
        subject="Neuer Mitarbeiter ab 01.11.2025",
        body="""Hallo IT, bitte alles für neuen Mitarbeiter Alexander Mayer vorbereiten. 
        Er erhält einen Laptop und ein Firmenhandy. 
        Eintrittsdatum ist der 01.11.2025. Danke!""",
    ),
}


def get_ticket_by_id(id: int) -> Ticket:
    """Get a ticket by its ID."""
    if id not in TICKET_DATASET:
        raise ValueError(f"Ticket ID {id} not recognized.")
    return TICKET_DATASET[id]
