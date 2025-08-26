from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime


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
            self.CHANGE_REQUEST: "Formal proposal to modify IT infrastructure, applications, or services",
            self.PROBLEM: "Underlying cause of one or more incidents requiring root cause analysis",
            self.INCIDENT: "Unplanned interruption or reduction in quality of an IT service",
        }
        return descriptions[self]


class TicketPriority(int, Enum):
    """Defines ticket priority levels due to issue impact and urgency."""

    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

    @property
    def description(self) -> str:
        descriptions = {
            self.CRITICAL: "Urgent issues needing immediate attention, causing major business disruption",
            self.HIGH: "Important issues to be addressed soon, potential for significant impact",
            self.MEDIUM: "Standard issues that can be scheduled for regular handling",
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
    """Defines the status of a ticket according to ITIL standards."""

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
    """Defines the area affected by the ticket."""

    HARDWARE = "hardware"
    SOFTWARE = "software"
    NETWORK = "network"
    ERP = "erp"
    DWH_BI = "datawarehouse_businessintelligence"
    SHAREPOINT = "sharepoint"
    PLANNER = "planner"
    TEAMS = "teams"
    EMAIL = "email"
    PRINTING = "printing"
    SECURITY = "security"

    @property
    def description(self) -> str:
        descriptions = {
            self.HARDWARE: "Issues with physical components (computers, phones, laptops, servers, peripherals)",
            self.SOFTWARE: "Issues with applications, operating systems, and software updates",
            self.NETWORK: "Network-related issues including LAN, WAN, WiFi, and VPN",
            self.ERP: "Issues with Microsoft Dynamics 365 Business Central and other ERP systems",
            self.DWH_BI: "Issues with data warehouse and PowerBI",
            self.SHAREPOINT: "Issues with SharePoint sites, permissions, and content",
            self.PLANNER: "Issues with Microsoft Planner tasks and boards",
            self.TEAMS: "Issues with Microsoft Teams calls, chats, and meetings",
            self.EMAIL: "Issues with Outlook, Calendar, Exchange, and email delivery",
            self.PRINTING: "Issues with printers, print servers, and scanning",
            self.SECURITY: "Issues with security tools, password manager, access, and compliance",
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
            self.IT_SUPPORT: "First level support team handling general IT issues and ticket triage",
            self.INFRASTRUCTURE_TEAM: "Support team for hardware, network, and infrastructure issues",
            self.APPLICATION_TEAM: "Team responsible for software applications and related issues",
            self.ERP_TEAM: "Specialized team for Dynamics 365 Business Central and ERP related issues",
            self.DWH_BI_TEAM: "Team managing data warehouse, ETL processes, and Business Intelligence tools like PowerBI",
        }
        return descriptions[self]


"""
This section defines the pydantic structured data model for the classification process.
"""


class TicketClassification(BaseModel):
    """Classification details for a ticket. Includes type, priority, sentiment, tags, responsible team and additional information."""

    ticket_type: TicketType = Field(..., description="Type of the ticket")
    ticket_priority: TicketPriority = Field(
        ..., description="Priority level of the ticket"
    )
    ticket_sentiment: TicketSentiment = Field(
        ..., description="Sentiment of the ticket submitter"
    )
    ticket_tags: Optional[List[TicketTags]] = Field(
        default=None, max_items=3, description="Tags associated with the ticket"
    )
    responsible_team: Optional[ResponsibleTeam] = Field(
        default=ResponsibleTeam.IT_SUPPORT
    )
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score for the classification action (between 0.0 and 1.0)",
    )
    key_information: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Key information extracted from the ticket",
    )
    suggested_action: Optional[str] = Field(
        default=None,
        max_length=2000,
        description="Suggested action to be taken for the ticket",
    )
    reasoning: Optional[str] = Field(
        default=None,
        max_length=2000,
        description="Reasoning behind the classification and suggested action",
    )

    @property
    def is_confident(self) -> bool:
        """Returns True if confidence score is above 0.8"""
        return self.confidence_score > 0.85


class Ticket(BaseModel):
    """Represents a support ticket."""

    id: str = Field(..., description="Unique identifier for the ticket")
    subject: str = Field(
        ..., min_length=1, max_length=100, description="Subject of the ticket"
    )
    body: Optional[str] = Field(None, max_length=1000, description="Body of the ticket")
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
    classified_at: Optional[str] = Field(
        default=None,
        description="ISO 8601 timestamp when the classification was performed",
    )

    @property
    def is_assigned(self) -> bool:
        return self.assigned_to is not None

    @property
    def is_classified(self) -> bool:
        return self.classification is not None

    def set_classification(self, classification: TicketClassification) -> None:
        self.classification = classification
        self.classified_at = datetime.now().isoformat()
        if self.is_classified and self.classification.is_confident:
            self.status = TicketStatus.OPEN
            self.assigned_to = self.classification.responsible_team.value
        else:
            self.status = TicketStatus.REVIEW_BY_HUMAN
