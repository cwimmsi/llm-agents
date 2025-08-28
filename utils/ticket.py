from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class TicketType(str, Enum):
    """ITIL-aligned ticket types."""

    SERVICE_REQUEST = "service_request"
    CHANGE_REQUEST = "change_request"
    PROBLEM = "problem"
    INCIDENT = "incident"

    @property
    def description(self) -> str:
        descriptions = {
            self.SERVICE_REQUEST: "Formal user request for information, advice, standard change, or access to services",
            self.CHANGE_REQUEST: "Formal proposal to modify existing IT infrastructure, applications, or services",
            self.PROBLEM: "Underlying cause of one or more incidents requiring root cause analysis",
            self.INCIDENT: "Unplanned interruption or reduction in quality of an IT service",
        }
        return descriptions[self]


class TicketPriority(str, Enum):
    """Defines ticket priority levels due to issue impact and urgency."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    @property
    def description(self) -> str:
        descriptions = {
            self.CRITICAL: "Urgent issues needing immediate attention, causing major business disruption for the entire company",
            self.HIGH: "Important issues to be addressed soon, potential for significant impact for one or a few employees",
            self.MEDIUM: "Standard issues that can be scheduled for regular handling, it's the default priority level",
            self.LOW: "Minor issues or requests that can be handled when convenient",
        }
        return descriptions[self]


class TicketSentiment(str, Enum):
    """Defines the sentiment of the ticket submitter."""

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"

    @property
    def description(self) -> str:
        descriptions = {
            self.POSITIVE: "User expresses satisfaction or happiness with the service",
            self.NEUTRAL: "User shows neither satisfaction nor dissatisfaction",
            self.NEGATIVE: "User expresses dissatisfaction, frustration, or anger",
        }
        return descriptions[self]


class TicketStatus(str, Enum):
    """Defines the status of a ticket."""

    NEW = "new"
    REVIEW_BY_HUMAN = "review_by_human"
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    RESOLVED = "resolved"
    CLOSED = "closed"

    @property
    def description(self) -> str:
        descriptions = {
            self.NEW: "Ticket has been created but not yet reviewed by support team",
            self.REVIEW_BY_HUMAN: "Ticket is being reviewed by a human agent for classification and assignment",
            self.OPEN: "Ticket has been reviewed and assigned",
            self.IN_PROGRESS: "Work is actively being done on the ticket",
            self.ON_HOLD: "Work is temporarily paused (waiting for user, third party, etc.)",
            self.RESOLVED: "Solution has been implemented and awaiting confirmation",
            self.CLOSED: "Ticket has been resolved and verified by the user",
        }
        return descriptions[self]


class TicketTags(str, Enum):
    """Defines tags associated with the ticket for better categorization."""

    HARDWARE = "hardware"
    SOFTWARE = "software"
    NETWORK = "network"
    PRINTING = "printing"
    SECURITY = "security"
    ONBOARDING = "onboarding"
    OFFBOARDING = "offboarding"

    @property
    def description(self) -> str:
        descriptions = {
            self.HARDWARE: "Issues with physical components (computers, phones, laptops, servers, peripherals)",
            self.SOFTWARE: "Issues with applications, operating systems, and software updates",
            self.NETWORK: "Network-related issues including LAN, WAN, WiFi, and VPN",
            self.PRINTING: "Issues with printers, print servers, and scanning",
            self.SECURITY: "Issues with security tools, password manager, access, and compliance",
            self.ONBOARDING: "Issues related to employee onboarding processes",
            self.OFFBOARDING: "Issues related to employee offboarding processes",
        }
        return descriptions[self]


class ResponsibleTeam(str, Enum):
    """Defines the team responsible for handling the ticket."""

    IT_SUPPORT = "it_support"
    INFRASTRUCTURE_TEAM = "infrastructure_team"
    APPLICATION_TEAM = "application_team"
    ERP_TEAM = "erp_team"
    DWH_BI_TEAM = "datawarehouse_businessintelligence_team"

    @property
    def description(self) -> str:
        descriptions = {
            self.IT_SUPPORT: "First level support team handling general IT issues, ticket triage, employee onboarding and offboarding",
            self.INFRASTRUCTURE_TEAM: "Specialized team for hardware, network, and infrastructure issues",
            self.APPLICATION_TEAM: "Specialized team responsible for software applications and related issues",
            self.ERP_TEAM: "Specialized team for Dynamics 365 Business Central and ERP related issues only",
            self.DWH_BI_TEAM: "Specialized team managing data warehouse and business intelligence tools like PowerBI",
        }
        return descriptions[self]


class TicketClassification(BaseModel):
    """Classification details for a ticket. To be filled by the LLM-Agent"""

    ticket_type: TicketType = Field(..., description="Type of the ticket")
    ticket_priority: TicketPriority = Field(
        ..., description="Priority level of the ticket"
    )
    ticket_sentiment: TicketSentiment = Field(
        ..., description="Sentiment of the ticket submitter"
    )
    ticket_tags: Optional[List[TicketTags]] = Field(
        default=None, description="Tags associated with the ticket"
    )
    responsible_team: Optional[ResponsibleTeam] = Field(
        default=ResponsibleTeam.IT_SUPPORT,
        description="Team responsible for handling the ticket",
    )
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score for the entire classification (between 0.0 and 1.0)",
    )
    suggested_action: Optional[str] = Field(
        default=None,
        description="Suggested action to be taken for the ticket",
    )
    reasoning: Optional[str] = Field(
        default=None,
        description="Reasoning behind the classification",
    )

    @property
    def is_confident(self) -> bool:
        """Returns True if confidence score is above 0.85"""
        return self.confidence_score > 0.85


class Ticket(BaseModel):
    """Represents a support ticket."""

    id: str = Field(..., description="Unique identifier for the ticket")
    subject: str = Field(
        ..., min_length=1, max_length=100, description="Subject of the ticket"
    )
    body: Optional[str] = Field(None, max_length=2000, description="Body of the ticket")
    status: TicketStatus = Field(
        default=TicketStatus.NEW, description="Status of the ticket"
    )
    assigned_to: Optional[str] = Field(
        None, description="Team or user to whom the ticket is assigned"
    )
    classification: TicketClassification = Field(
        None,
        description="Classification details for the ticket, provided by the LLM-Agent",
    )

    @property
    def is_classified(self) -> bool:
        return self.classification is not None

    def set_classification(self, classification: TicketClassification) -> None:
        self.classification = classification
        if self.is_classified and self.classification.is_confident:
            self.status = TicketStatus.OPEN
            self.assigned_to = self.classification.responsible_team.value
        else:
            self.status = TicketStatus.REVIEW_BY_HUMAN
