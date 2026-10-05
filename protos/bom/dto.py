from pydantic import BaseModel, Field


class ComponentNodeDTO(BaseModel):
    id: int
    name: str
    article: str = ""
    tier: int = 1
    country_code: str = "RU"
    manufacturer: str = ""
    hs_code: str = ""
    cost_rub: float = 0.0
    quantity: float = 1.0
    criticality: float = 1.0
    country_risk: float = 0.0
    analog_availability: float = 1.0
    cfi_score: float = 0.0
    is_chokepoint: bool = False
    parent_id: int | None = None
    children: list["ComponentNodeDTO"] = Field(default_factory=list)
    notes: str = ""


class GetBOMTreeResponseDTO(BaseModel):
    product_id: int
    product_name: str
    root: ComponentNodeDTO | None = None
    total_cost_rub: float = 0.0
    paper_localization_pct: float = 0.0
    defacto_localization_pct: float = 0.0
    total_components: int = 0
    chokepoints_count: int = 0
    overall_cfi_max: float = 0.0


class AnalogOptionDTO(BaseModel):
    analog_id: int
    name: str
    manufacturer: str
    country_code: str
    unit_cost_rub: float
    redesign_cost_rub: float
    lead_time_days: int
    compatibility_score: float
    description: str = ""


class SimulateAnalogSubstitutionDTO(BaseModel):
    component_id: int
    analog_id: int


class SimulateAnalogResponseDTO(BaseModel):
    success: bool
    component_id: int
    old_cfi: float
    new_cfi: float
    new_defacto_localization_pct: float
    cost_delta_rub: float
    redesign_investment_rub: float
    implementation_days: int
    commentary: str
