from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluatePP719Request(_message.Message):
    __slots__ = ("product_id", "industry_code")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    industry_code: str
    def __init__(self, product_id: _Optional[int] = ..., industry_code: _Optional[str] = ...) -> None: ...

class EvaluatePP719Response(_message.Message):
    __slots__ = ("product_id", "is_compliant", "achieved_points", "required_points", "ad_valorem_pct", "required_ad_valorem_pct", "operation_breakdown", "status_decision", "certificate_recommendation")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLIANT_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_POINTS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_POINTS_FIELD_NUMBER: _ClassVar[int]
    AD_VALOREM_PCT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_AD_VALOREM_PCT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    STATUS_DECISION_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    is_compliant: bool
    achieved_points: int
    required_points: int
    ad_valorem_pct: float
    required_ad_valorem_pct: float
    operation_breakdown: _containers.RepeatedCompositeFieldContainer[PointBreakdown]
    status_decision: str
    certificate_recommendation: str
    def __init__(self, product_id: _Optional[int] = ..., is_compliant: bool = ..., achieved_points: _Optional[int] = ..., required_points: _Optional[int] = ..., ad_valorem_pct: _Optional[float] = ..., required_ad_valorem_pct: _Optional[float] = ..., operation_breakdown: _Optional[_Iterable[_Union[PointBreakdown, _Mapping]]] = ..., status_decision: _Optional[str] = ..., certificate_recommendation: _Optional[str] = ...) -> None: ...

class PointBreakdown(_message.Message):
    __slots__ = ("operation_name", "points_awarded", "verified", "evidence_doc")
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_AWARDED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_DOC_FIELD_NUMBER: _ClassVar[int]
    operation_name: str
    points_awarded: int
    verified: bool
    evidence_doc: str
    def __init__(self, operation_name: _Optional[str] = ..., points_awarded: _Optional[int] = ..., verified: bool = ..., evidence_doc: _Optional[str] = ...) -> None: ...

class AuditDeFactoRequest(_message.Message):
    __slots__ = ("product_id", "include_chokepoints")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHOKEPOINTS_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    include_chokepoints: bool
    def __init__(self, product_id: _Optional[int] = ..., include_chokepoints: bool = ...) -> None: ...

class AuditDeFactoResponse(_message.Message):
    __slots__ = ("product_id", "paper_localization_pct", "defacto_localization_pct", "vulnerability_gap_pct", "critical_chokepoints_found", "chokepoints", "o_ring_summary")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PAPER_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    DEFACTO_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_GAP_PCT_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_CHOKEPOINTS_FOUND_FIELD_NUMBER: _ClassVar[int]
    CHOKEPOINTS_FIELD_NUMBER: _ClassVar[int]
    O_RING_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    paper_localization_pct: float
    defacto_localization_pct: float
    vulnerability_gap_pct: float
    critical_chokepoints_found: int
    chokepoints: _containers.RepeatedCompositeFieldContainer[ChokepointItem]
    o_ring_summary: str
    def __init__(self, product_id: _Optional[int] = ..., paper_localization_pct: _Optional[float] = ..., defacto_localization_pct: _Optional[float] = ..., vulnerability_gap_pct: _Optional[float] = ..., critical_chokepoints_found: _Optional[int] = ..., chokepoints: _Optional[_Iterable[_Union[ChokepointItem, _Mapping]]] = ..., o_ring_summary: _Optional[str] = ...) -> None: ...

class ChokepointItem(_message.Message):
    __slots__ = ("component_id", "component_name", "tier", "country", "cost_rub", "cfi_score", "risk_reason", "potential_paralysis_scope")
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COST_RUB_FIELD_NUMBER: _ClassVar[int]
    CFI_SCORE_FIELD_NUMBER: _ClassVar[int]
    RISK_REASON_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_PARALYSIS_SCOPE_FIELD_NUMBER: _ClassVar[int]
    component_id: int
    component_name: str
    tier: int
    country: str
    cost_rub: float
    cfi_score: float
    risk_reason: str
    potential_paralysis_scope: str
    def __init__(self, component_id: _Optional[int] = ..., component_name: _Optional[str] = ..., tier: _Optional[int] = ..., country: _Optional[str] = ..., cost_rub: _Optional[float] = ..., cfi_score: _Optional[float] = ..., risk_reason: _Optional[str] = ..., potential_paralysis_scope: _Optional[str] = ...) -> None: ...

class SimulateSanctionsShockRequest(_message.Message):
    __slots__ = ("product_id", "blocked_countries", "blocked_categories", "enforce_secondary_sanctions")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_SECONDARY_SANCTIONS_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    blocked_countries: _containers.RepeatedScalarFieldContainer[str]
    blocked_categories: _containers.RepeatedScalarFieldContainer[str]
    enforce_secondary_sanctions: bool
    def __init__(self, product_id: _Optional[int] = ..., blocked_countries: _Optional[_Iterable[str]] = ..., blocked_categories: _Optional[_Iterable[str]] = ..., enforce_secondary_sanctions: bool = ...) -> None: ...

class SimulateSanctionsShockResponse(_message.Message):
    __slots__ = ("product_id", "shock_name", "production_paralysis_risk_pct", "blocked_components_count", "blocked_value_rub", "blocked_items", "estimated_days_until_stockout", "mitigation_roadmap")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SHOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_PARALYSIS_RISK_PCT_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_COMPONENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_VALUE_RUB_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DAYS_UNTIL_STOCKOUT_FIELD_NUMBER: _ClassVar[int]
    MITIGATION_ROADMAP_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    shock_name: str
    production_paralysis_risk_pct: float
    blocked_components_count: int
    blocked_value_rub: float
    blocked_items: _containers.RepeatedCompositeFieldContainer[ChokepointItem]
    estimated_days_until_stockout: int
    mitigation_roadmap: str
    def __init__(self, product_id: _Optional[int] = ..., shock_name: _Optional[str] = ..., production_paralysis_risk_pct: _Optional[float] = ..., blocked_components_count: _Optional[int] = ..., blocked_value_rub: _Optional[float] = ..., blocked_items: _Optional[_Iterable[_Union[ChokepointItem, _Mapping]]] = ..., estimated_days_until_stockout: _Optional[int] = ..., mitigation_roadmap: _Optional[str] = ...) -> None: ...

class GenerateGeopoliticalScenarioRequest(_message.Message):
    __slots__ = ("event_description", "target_industry", "product_id")
    EVENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    event_description: str
    target_industry: str
    product_id: int
    def __init__(self, event_description: _Optional[str] = ..., target_industry: _Optional[str] = ..., product_id: _Optional[int] = ...) -> None: ...

class GenerateGeopoliticalScenarioResponse(_message.Message):
    __slots__ = ("scenario_id", "scenario_title", "ai_executive_summary", "dynamic_policy_json", "calculated_impact_severity", "affected_supply_chains", "recommended_urgent_actions")
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_TITLE_FIELD_NUMBER: _ClassVar[int]
    AI_EXECUTIVE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_POLICY_JSON_FIELD_NUMBER: _ClassVar[int]
    CALCULATED_IMPACT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_SUPPLY_CHAINS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_URGENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    scenario_id: str
    scenario_title: str
    ai_executive_summary: str
    dynamic_policy_json: str
    calculated_impact_severity: float
    affected_supply_chains: _containers.RepeatedScalarFieldContainer[str]
    recommended_urgent_actions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scenario_id: _Optional[str] = ..., scenario_title: _Optional[str] = ..., ai_executive_summary: _Optional[str] = ..., dynamic_policy_json: _Optional[str] = ..., calculated_impact_severity: _Optional[float] = ..., affected_supply_chains: _Optional[_Iterable[str]] = ..., recommended_urgent_actions: _Optional[_Iterable[str]] = ...) -> None: ...
