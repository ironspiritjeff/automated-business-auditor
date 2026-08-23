from enum import Enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class DepartmentRoutingTag(str, Enum):
    LEGAL = "legal"
    FINANCE = "finance"
    OPERATIONS = "operations"
    HR = "human_resources"


class ProcessingStatus(str, Enum):
    STAGED = "staged"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class AuditUploadRequest(BaseModel):
    filename: str = Field(
        ...,
        min_length=5,
        max_length=255,
        pattern=r"^.*\.pdf$",
        description="The original PDF file name being staged for processing."
    )
    raw_character_count: int = Field(
        ...,
        gt=0,
        le=5_000_000,
        description="The strict character threshold count extracted from the document text layout."
    )
    department_routing: DepartmentRoutingTag = Field(
        ...,
        description="The business department responsible for reviewing the compliance flags."
    )


class AuditDocumentRecord(BaseModel):
    document_id: UUID = Field(
        ...,
        description="The unique system-generated identifier for tracing this audit asset."
    )
    filename: str = Field(
        ...,
        description="The validated file name of the compliance asset."
    )
    raw_character_count: int = Field(
        ...,
        description="The verified length of the process text."
    )
    department_routing: DepartmentRoutingTag = Field(
        ...,
        description="The assigned business department router tier."
    )
    status: ProcessingStatus = Field(
        ...,
        description="The progressive processing milestone flag within the AI processing pipeline."
    )
    created_at: datetime = Field(
        ...,
        description="The ISO timestamp indicating when this record was staged in the system."
    )
