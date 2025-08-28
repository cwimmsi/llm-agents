from typing import Dict
from utils.ticket import Ticket


TICKET_DATASET: Dict[int, Ticket] = {
    1: Ticket(
        id="TKT-001",
        subject="WLAN ausgefallen",
        body="""Ich und mein Team haben kein Internet. Weder auf dem Laptop noch auf dem Handy. 
        Bei unseren Kollegen im anderen Gebäude funktioniert es auch nicht. Bitte um schnelle Behebung des Problems!
        Wir müssen dringend Rechnungen versenden.""",
    ),
    2: Ticket(
        id="TKT-002",
        subject="OneDrive Datei kann nicht geöffnet werden",
        body="""Wenn ich eine Datei in OneDrive lokal öffne, kommt die Fehlermeldung, dass der Dateipfad zu lang ist.""",
    ),
    3: Ticket(
        id="TKT-003",
        subject="PDFXChange installieren",
        body="""Hallo, ich brauche den PDFXChange auf meinem Laptop. Könnt ihr mir diesen bitte installieren.""",
    ),
    4: Ticket(
        id="TKT-004",
        subject="Neuer Mitarbeiter ab 01.11.2025",
        body="""Hallo IT, bitte alles für unseren neuen Mitarbeiter in der Abteilung Kalkulation vorbereiten. 
        Er erhält einen Laptop und ein Firmenhandy. Die Programme und Zugänge gleich einrichten, wie bei den anderen Kollegen der Abteilung.
        Eintrittsdatum ist der 01.11.2025. Danke!""",
    ),
    5: Ticket(
        id="TKT-005",
        subject="Power BI Bericht Datenquelle erweitern",
        body="""Wir brauchen zusätzliche Daten in der Datenquelle für unseren KORE Power BI Bericht.
        Die benötigten Buchungen sind die Verkaufsbuchungen. Bitte um Rückmeldung wie bald ihr das umsetzen könnt.
        Für weitere Fragen meldet euch in der KORE Abteilung. Danke.""",
    ),
    6: Ticket(
        id="TKT-006",
        subject="Drucker übersiedeln vom IT Büro ins QM Büro",
        body="""Wie letztens besprochen, möchten wir den Drucker aus dem IT Büro ins QM Büro stellen.
        Bitte bei Gelegenheit alles vorbereiten und durchführen.
        """,
    ),
    7: Ticket(
        id="TKT-007",
        subject="Handy Display kaputt",
        body="""Hallo IT, mein Firmenhandy ist auf den Boden gefallen und jetzt ist das Display kaputt.
        Es hat mehrere Risse und funktioniert nicht mehr richtig. Ich brauche bitte ein Ersatzgerät.
        """,
    ),
}


def get_ticket_by_id(id: int) -> Ticket:
    """Get a ticket by its ID."""
    if id not in TICKET_DATASET:
        raise ValueError(f"Ticket ID {id} not recognized.")
    return TICKET_DATASET[id]
