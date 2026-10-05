from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WriteAuditEventRequest(_message.Message):
    __slots__ = ("event_type", "actor_id", "actor_role", "resource_type", "resource_id", "details_json", "ip_address")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ROLE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_JSON_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    actor_id: int
    actor_role: str
    resource_type: str
    resource_id: int
    details_json: str
    ip_address: str
    def __init__(self, event_type: _Optional[str] = ..., actor_id: _Optional[int] = ..., actor_role: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[int] = ..., details_json: _Optional[str] = ..., ip_address: _Optional[str] = ...) -> None: ...

class WriteAuditEventResponse(_message.Message):
    __slots__ = ("success", "audit_id", "hash_sha256", "recorded_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    HASH_SHA256_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    audit_id: int
    hash_sha256: str
    recorded_at: str
    def __init__(self, success: bool = ..., audit_id: _Optional[int] = ..., hash_sha256: _Optional[str] = ..., recorded_at: _Optional[str] = ...) -> None: ...

class QueryAuditTrailRequest(_message.Message):
    __slots__ = ("resource_type", "resource_id", "date_from", "date_to", "limit", "offset")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    resource_id: int
    date_from: str
    date_to: str
    limit: int
    offset: int
    def __init__(self, resource_type: _Optional[str] = ..., resource_id: _Optional[int] = ..., date_from: _Optional[str] = ..., date_to: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class AuditRecord(_message.Message):
    __slots__ = ("id", "event_type", "actor_id", "actor_role", "resource_type", "resource_id", "details_json", "recorded_at", "hash_sha256")
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ROLE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_JSON_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    HASH_SHA256_FIELD_NUMBER: _ClassVar[int]
    id: int
    event_type: str
    actor_id: int
    actor_role: str
    resource_type: str
    resource_id: int
    details_json: str
    recorded_at: str
    hash_sha256: str
    def __init__(self, id: _Optional[int] = ..., event_type: _Optional[str] = ..., actor_id: _Optional[int] = ..., actor_role: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[int] = ..., details_json: _Optional[str] = ..., recorded_at: _Optional[str] = ..., hash_sha256: _Optional[str] = ...) -> None: ...

class QueryAuditTrailResponse(_message.Message):
    __slots__ = ("records", "total_count")
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[AuditRecord]
    total_count: int
    def __init__(self, records: _Optional[_Iterable[_Union[AuditRecord, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class IssueCertificateRequest(_message.Message):
    __slots__ = ("product_id", "certificate_type", "valid_months", "certified_by")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALID_MONTHS_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    certificate_type: str
    valid_months: int
    certified_by: str
    def __init__(self, product_id: _Optional[int] = ..., certificate_type: _Optional[str] = ..., valid_months: _Optional[int] = ..., certified_by: _Optional[str] = ...) -> None: ...

class IssueCertificateResponse(_message.Message):
    __slots__ = ("is_issued", "certificate_number", "qr_verification_url", "issued_at", "expires_at", "certified_defacto_loc", "certified_points", "digital_signature_hash")
    IS_ISSUED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    QR_VERIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_DEFACTO_LOC_FIELD_NUMBER: _ClassVar[int]
    CERTIFIED_POINTS_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_SIGNATURE_HASH_FIELD_NUMBER: _ClassVar[int]
    is_issued: bool
    certificate_number: str
    qr_verification_url: str
    issued_at: str
    expires_at: str
    certified_defacto_loc: float
    certified_points: int
    digital_signature_hash: str
    def __init__(self, is_issued: bool = ..., certificate_number: _Optional[str] = ..., qr_verification_url: _Optional[str] = ..., issued_at: _Optional[str] = ..., expires_at: _Optional[str] = ..., certified_defacto_loc: _Optional[float] = ..., certified_points: _Optional[int] = ..., digital_signature_hash: _Optional[str] = ...) -> None: ...
