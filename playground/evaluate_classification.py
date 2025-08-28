from utils.ticket import TicketClassification
from utils.logger import setup_logger


def evaluate_classification(
    actual_classification: TicketClassification,
    expected_classification: TicketClassification,
    ticket_id: str,
) -> int:
    """Perform evaluation of the classified ticket against the expected ticket."""
    logger = setup_logger()

    score = 5

    if actual_classification.ticket_type != expected_classification.ticket_type:
        logger.warning(
            f"{ticket_id}: Discrepancy actual: {actual_classification.ticket_type} <> expected: {expected_classification.ticket_type}"
        )
        score -= 1

    if actual_classification.ticket_priority != expected_classification.ticket_priority:
        logger.warning(
            f"{ticket_id}: Discrepancy actual: {actual_classification.ticket_priority} <> expected: {expected_classification.ticket_priority}"
        )
        score -= 1

    if (
        actual_classification.ticket_sentiment
        != expected_classification.ticket_sentiment
    ):
        logger.warning(
            f"{ticket_id}: Discrepancy actual: {actual_classification.ticket_sentiment} <> expected: {expected_classification.ticket_sentiment}"
        )
        score -= 1

    if actual_classification.ticket_tags != expected_classification.ticket_tags:
        logger.warning(
            f"{ticket_id}: Discrepancy actual: {actual_classification.ticket_tags} <> expected: {expected_classification.ticket_tags}"
        )
        score -= 1

    if (
        actual_classification.responsible_team
        != expected_classification.responsible_team
    ):
        logger.warning(
            f"{ticket_id}: Discrepancy actual: {actual_classification.responsible_team} <> expected: {expected_classification.responsible_team}"
        )
        score -= 1

    return score
