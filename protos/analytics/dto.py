from pydantic import BaseModel, Field
from datetime import datetime


class AuditLedgerEventDTO(BaseModel):
    event_id: str
    timestamp: str
    trace_id: str
    product_id: int
    product_name: str
    event_type: str  # 'BOM_MUTATION', 'PP719_AUDIT', 'SHOCK_TRIGGERED', 'CERT_ISSUED'
    actor_type: str  # 'ENTERPRISE_USER', 'REGULATOR_MINPROMTORG', 'AI_ORACLE'
    paper_localization_pct: float
    defacto_localization_pct: float
    vulnerability_gap_pct: float
    chokepoints_count: int
    digital_signature: str
    payload_json: str = "{}"


class RecordEventResponseDTO(BaseModel):
    success: bool
    event_id: str
    message: str


class MonteCarloIterationDTO(BaseModel):
    iteration: int
    is_paralyzed: bool
    days_to_halt: int
    loss_rub: float
    failed_chokepoint: str


class MonteCarloSimulationResponseDTO(BaseModel):
    run_id: str
    product_id: int
    total_iterations: int
    paralysis_probability_pct: float
    median_days_to_halt: float
    value_at_risk_rub: float
    sample_iterations: list[MonteCarloIterationDTO] = Field(default_factory=list)
    executive_summary: str


class TimeSeriesDataPointDTO(BaseModel):
    timestamp: str
    paper_localization_pct: float
    defacto_localization_pct: float


class AnalyticsSummaryDTO(BaseModel):
    product_id: int
    total_events_recorded: int
    current_vulnerability_gap_pct: float
    active_chokepoints_count: int
    localization_trend: list[TimeSeriesDataPointDTO] = Field(default_factory=list)
    storage_engine: str = "ClickHouse (ReplacingMergeTree)"
