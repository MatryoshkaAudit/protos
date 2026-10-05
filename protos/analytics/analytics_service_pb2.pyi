from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditEventMessage(_message.Message):
    __slots__ = ("event_id", "timestamp", "trace_id", "product_id", "product_name", "event_type", "actor_type", "paper_localization_pct", "defacto_localization_pct", "vulnerability_gap_pct", "chokepoints_count", "digital_signature", "payload_json")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAPER_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    DEFACTO_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_GAP_PCT_FIELD_NUMBER: _ClassVar[int]
    CHOKEPOINTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    timestamp: str
    trace_id: str
    product_id: int
    product_name: str
    event_type: str
    actor_type: str
    paper_localization_pct: float
    defacto_localization_pct: float
    vulnerability_gap_pct: float
    chokepoints_count: int
    digital_signature: str
    payload_json: str
    def __init__(self, event_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., trace_id: _Optional[str] = ..., product_id: _Optional[int] = ..., product_name: _Optional[str] = ..., event_type: _Optional[str] = ..., actor_type: _Optional[str] = ..., paper_localization_pct: _Optional[float] = ..., defacto_localization_pct: _Optional[float] = ..., vulnerability_gap_pct: _Optional[float] = ..., chokepoints_count: _Optional[int] = ..., digital_signature: _Optional[str] = ..., payload_json: _Optional[str] = ...) -> None: ...

class RecordEventRequest(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: AuditEventMessage
    def __init__(self, event: _Optional[_Union[AuditEventMessage, _Mapping]] = ...) -> None: ...

class RecordEventResponse(_message.Message):
    __slots__ = ("success", "event_id", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    event_id: str
    message: str
    def __init__(self, success: bool = ..., event_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetLedgerEventsRequest(_message.Message):
    __slots__ = ("product_id", "limit")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    limit: int
    def __init__(self, product_id: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetLedgerEventsResponse(_message.Message):
    __slots__ = ("events", "total_count")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AuditEventMessage]
    total_count: int
    def __init__(self, events: _Optional[_Iterable[_Union[AuditEventMessage, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class RunMonteCarloRequest(_message.Message):
    __slots__ = ("product_id", "iterations_count", "blocked_countries")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    iterations_count: int
    blocked_countries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, product_id: _Optional[int] = ..., iterations_count: _Optional[int] = ..., blocked_countries: _Optional[_Iterable[str]] = ...) -> None: ...

class MonteCarloIterationResult(_message.Message):
    __slots__ = ("iteration", "is_paralyzed", "days_to_halt", "loss_rub", "failed_chokepoint")
    ITERATION_FIELD_NUMBER: _ClassVar[int]
    IS_PARALYZED_FIELD_NUMBER: _ClassVar[int]
    DAYS_TO_HALT_FIELD_NUMBER: _ClassVar[int]
    LOSS_RUB_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHOKEPOINT_FIELD_NUMBER: _ClassVar[int]
    iteration: int
    is_paralyzed: bool
    days_to_halt: int
    loss_rub: float
    failed_chokepoint: str
    def __init__(self, iteration: _Optional[int] = ..., is_paralyzed: bool = ..., days_to_halt: _Optional[int] = ..., loss_rub: _Optional[float] = ..., failed_chokepoint: _Optional[str] = ...) -> None: ...

class RunMonteCarloResponse(_message.Message):
    __slots__ = ("run_id", "product_id", "total_iterations", "paralysis_probability_pct", "median_days_to_halt", "value_at_risk_rub", "sample_iterations", "executive_summary")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARALYSIS_PROBABILITY_PCT_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_DAYS_TO_HALT_FIELD_NUMBER: _ClassVar[int]
    VALUE_AT_RISK_RUB_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTIVE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    product_id: int
    total_iterations: int
    paralysis_probability_pct: float
    median_days_to_halt: float
    value_at_risk_rub: float
    sample_iterations: _containers.RepeatedCompositeFieldContainer[MonteCarloIterationResult]
    executive_summary: str
    def __init__(self, run_id: _Optional[str] = ..., product_id: _Optional[int] = ..., total_iterations: _Optional[int] = ..., paralysis_probability_pct: _Optional[float] = ..., median_days_to_halt: _Optional[float] = ..., value_at_risk_rub: _Optional[float] = ..., sample_iterations: _Optional[_Iterable[_Union[MonteCarloIterationResult, _Mapping]]] = ..., executive_summary: _Optional[str] = ...) -> None: ...

class GetAnalyticsSummaryRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class TimeSeriesDataPoint(_message.Message):
    __slots__ = ("timestamp", "paper_localization_pct", "defacto_localization_pct")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAPER_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    DEFACTO_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    paper_localization_pct: float
    defacto_localization_pct: float
    def __init__(self, timestamp: _Optional[str] = ..., paper_localization_pct: _Optional[float] = ..., defacto_localization_pct: _Optional[float] = ...) -> None: ...

class GetAnalyticsSummaryResponse(_message.Message):
    __slots__ = ("product_id", "total_events_recorded", "current_vulnerability_gap_pct", "active_chokepoints_count", "localization_trend", "storage_engine")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EVENTS_RECORDED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VULNERABILITY_GAP_PCT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CHOKEPOINTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_TREND_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ENGINE_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    total_events_recorded: int
    current_vulnerability_gap_pct: float
    active_chokepoints_count: int
    localization_trend: _containers.RepeatedCompositeFieldContainer[TimeSeriesDataPoint]
    storage_engine: str
    def __init__(self, product_id: _Optional[int] = ..., total_events_recorded: _Optional[int] = ..., current_vulnerability_gap_pct: _Optional[float] = ..., active_chokepoints_count: _Optional[int] = ..., localization_trend: _Optional[_Iterable[_Union[TimeSeriesDataPoint, _Mapping]]] = ..., storage_engine: _Optional[str] = ...) -> None: ...
