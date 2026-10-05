from pydantic import BaseModel, Field


class WriteAuditEventDTO(BaseModel):
    event_type: str
    actor_id: int
    actor_role: str = "engineer"
    resource_type: str
    resource_id: int
    details_json: str = "{}"
    ip_address: str = "127.0.0.1"


class WriteAuditEventResponseDTO(BaseModel):
    success: bool
    audit_id: int
    hash_sha256: str
    recorded_at: str


class AuditRecordDTO(BaseModel):
    id: int
    event_type: str
    actor_id: int
    actor_role: str
    resource_type: str
    resource_id: int
    details_json: str
    recorded_at: str
    hash_sha256: str


class QueryAuditTrailResponseDTO(BaseModel):
    records: list[AuditRecordDTO] = Field(default_factory=list)
    total_count: int = 0


class IssueCertificateDTO(BaseModel):
    product_id: int
    certificate_type: str = "PP_719_ORIGIN"
    valid_months: int = 12
    certified_by: str = "Минпромторг РФ"


class IssueCertificateResponseDTO(BaseModel):
    is_issued: bool
    certificate_number: str
    qr_verification_url: str
    issued_at: str
    expires_at: str
    certified_defacto_loc: float
    certified_points: int
    digital_signature_hash: str
