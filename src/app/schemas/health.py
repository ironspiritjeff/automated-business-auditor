from typing import Literal
from pydantic import BaseModel, Field

class HealthCheckResponse(BaseModel):
    """
    Strict data validation schema for the system health check gateway.
    
    Guarantees structured system telemetry parameters are returned 
    identically across development, staging, and production clusters.
    """
    status: Literal["healthy", "unhealthy", "degraded"] = Field(
        ..., 
        description="The operational performance state of the API microservice layer."
    )
    service_name: str = Field(
        ..., 
        description="The formal microservice identifier."
    )
    environment_tier: str = Field(
        ..., 
        description="The current cloud cluster hosting tier environment."
    )
