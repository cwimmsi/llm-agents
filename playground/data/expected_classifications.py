from typing import Dict
from utils.ticket import (
    TicketClassification,
    TicketType,
    TicketPriority,
    TicketSentiment,
    TicketTags,
    ResponsibleTeam,
)


EXPECTED_CLASSIFICATIONS: Dict[int, TicketClassification] = {
    1: TicketClassification(
        ticket_type=TicketType.INCIDENT,
        ticket_priority=TicketPriority.CRITICAL,
        ticket_sentiment=TicketSentiment.NEGATIVE,
        ticket_tags=[TicketTags.NETWORK],
        responsible_team=ResponsibleTeam.HARDWARE_NETWORK_TEAM,
        confidence_score=1.0,
    ),
    2: TicketClassification(
        ticket_type=TicketType.INCIDENT,
        ticket_priority=TicketPriority.HIGH,
        ticket_sentiment=TicketSentiment.NEGATIVE,
        ticket_tags=[TicketTags.SOFTWARE],
        responsible_team=ResponsibleTeam.SOFTWARE_TEAM,
        confidence_score=1.0,
    ),
    3: TicketClassification(
        ticket_type=TicketType.SERVICE_REQUEST,
        ticket_priority=TicketPriority.MEDIUM,
        ticket_sentiment=TicketSentiment.NEUTRAL,
        ticket_tags=[TicketTags.SOFTWARE],
        responsible_team=ResponsibleTeam.SOFTWARE_TEAM,
        confidence_score=1.0,
    ),
    4: TicketClassification(
        ticket_type=TicketType.SERVICE_REQUEST,
        ticket_priority=TicketPriority.MEDIUM,
        ticket_sentiment=TicketSentiment.POSITIVE,
        ticket_tags=[TicketTags.ONBOARDING],
        responsible_team=ResponsibleTeam.IT_SUPPORT,
        confidence_score=1.0,
    ),
    5: TicketClassification(
        ticket_type=TicketType.CHANGE_REQUEST,
        ticket_priority=TicketPriority.MEDIUM,
        ticket_sentiment=TicketSentiment.NEUTRAL,
        ticket_tags=[TicketTags.SOFTWARE],
        responsible_team=ResponsibleTeam.DWH_BI_TEAM,
        confidence_score=1.0,
    ),
    6: TicketClassification(
        ticket_type=TicketType.CHANGE_REQUEST,
        ticket_priority=TicketPriority.MEDIUM,
        ticket_sentiment=TicketSentiment.NEUTRAL,
        ticket_tags=[TicketTags.PRINTING],
        responsible_team=ResponsibleTeam.HARDWARE_NETWORK_TEAM,
        confidence_score=1.0,
    ),
    7: TicketClassification(
        ticket_type=TicketType.SERVICE_REQUEST,
        ticket_priority=TicketPriority.HIGH,
        ticket_sentiment=TicketSentiment.NEUTRAL,
        ticket_tags=[TicketTags.HARDWARE],
        responsible_team=ResponsibleTeam.HARDWARE_NETWORK_TEAM,
        confidence_score=1.0,
    ),
}


def get_expected_classification(id: int) -> TicketClassification:
    """Get the expected classification for a ticket by its ID."""
    if id not in EXPECTED_CLASSIFICATIONS:
        raise ValueError(f"Ticket classification {id} not recognized.")
    return EXPECTED_CLASSIFICATIONS[id]
