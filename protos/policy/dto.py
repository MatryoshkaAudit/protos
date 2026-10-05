from pydantic import BaseModel, Field


class PointBreakdownDTO(BaseModel):
    operation_name: str
    points_awarded: int
    verified: bool = True
    evidence_doc: str = ""


class EvaluatePP719ResponseDTO(BaseModel):
    product_id: int
    is_compliant: bool
    achieved_points: int
    required_points: int
    ad_valorem_pct: float
    required_ad_valorem_pct: float
    operation_breakdown: list[PointBreakdownDTO] = Field(default_factory=list)
    status_decision: str
    certificate_recommendation: str


class ChokepointItemDTO(BaseModel):
    component_id: int
    component_name: str
    tier: int
    country: str
    cost_rub: float
    cfi_score: float
    risk_reason: str
    potential_paralysis_scope: str


class AuditDeFactoResponseDTO(BaseModel):
    product_id: int
    paper_localization_pct: float
    defacto_localization_pct: float
    vulnerability_gap_pct: float
    critical_chokepoints_found: int
    chokepoints: list[ChokepointItemDTO] = Field(default_factory=list)
    o_ring_summary: str


class SimulateSanctionsShockDTO(BaseModel):
    product_id: int
    blocked_countries: list[str] = Field(default_factory=list)
    blocked_categories: list[str] = Field(default_factory=list)
    enforce_secondary_sanctions: bool = True


class SimulateSanctionsShockResponseDTO(BaseModel):
    product_id: int
    shock_name: str
    production_paralysis_risk_pct: float
    blocked_components_count: int
    blocked_value_rub: float
    blocked_items: list[ChokepointItemDTO] = Field(default_factory=list)
    estimated_days_until_stockout: int
    mitigation_roadmap: str


class GenerateGeopoliticalScenarioResponseDTO(BaseModel):
    scenario_id: str
    scenario_title: str
    ai_executive_summary: str
    dynamic_policy_json: str
    calculated_impact_severity: float
    affected_supply_chains: list[str] = Field(default_factory=list)
    recommended_urgent_actions: list[str] = Field(default_factory=list)
