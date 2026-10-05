from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComponentNode(_message.Message):
    __slots__ = ("id", "name", "article", "tier", "country_code", "manufacturer", "hs_code", "cost_rub", "quantity", "criticality", "country_risk", "analog_availability", "cfi_score", "is_chokepoint", "parent_id", "children", "notes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    HS_CODE_FIELD_NUMBER: _ClassVar[int]
    COST_RUB_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CRITICALITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_RISK_FIELD_NUMBER: _ClassVar[int]
    ANALOG_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CFI_SCORE_FIELD_NUMBER: _ClassVar[int]
    IS_CHOKEPOINT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    article: str
    tier: int
    country_code: str
    manufacturer: str
    hs_code: str
    cost_rub: float
    quantity: float
    criticality: float
    country_risk: float
    analog_availability: float
    cfi_score: float
    is_chokepoint: bool
    parent_id: int
    children: _containers.RepeatedCompositeFieldContainer[ComponentNode]
    notes: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., article: _Optional[str] = ..., tier: _Optional[int] = ..., country_code: _Optional[str] = ..., manufacturer: _Optional[str] = ..., hs_code: _Optional[str] = ..., cost_rub: _Optional[float] = ..., quantity: _Optional[float] = ..., criticality: _Optional[float] = ..., country_risk: _Optional[float] = ..., analog_availability: _Optional[float] = ..., cfi_score: _Optional[float] = ..., is_chokepoint: bool = ..., parent_id: _Optional[int] = ..., children: _Optional[_Iterable[_Union[ComponentNode, _Mapping]]] = ..., notes: _Optional[str] = ...) -> None: ...

class GetBOMTreeRequest(_message.Message):
    __slots__ = ("product_id", "include_analogs")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ANALOGS_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    include_analogs: bool
    def __init__(self, product_id: _Optional[int] = ..., include_analogs: bool = ...) -> None: ...

class GetBOMTreeResponse(_message.Message):
    __slots__ = ("product_id", "product_name", "root", "total_cost_rub", "paper_localization_pct", "defacto_localization_pct", "total_components", "chokepoints_count", "overall_cfi_max")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_RUB_FIELD_NUMBER: _ClassVar[int]
    PAPER_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    DEFACTO_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    CHOKEPOINTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    OVERALL_CFI_MAX_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    product_name: str
    root: ComponentNode
    total_cost_rub: float
    paper_localization_pct: float
    defacto_localization_pct: float
    total_components: int
    chokepoints_count: int
    overall_cfi_max: float
    def __init__(self, product_id: _Optional[int] = ..., product_name: _Optional[str] = ..., root: _Optional[_Union[ComponentNode, _Mapping]] = ..., total_cost_rub: _Optional[float] = ..., paper_localization_pct: _Optional[float] = ..., defacto_localization_pct: _Optional[float] = ..., total_components: _Optional[int] = ..., chokepoints_count: _Optional[int] = ..., overall_cfi_max: _Optional[float] = ...) -> None: ...

class ComponentDetailRequest(_message.Message):
    __slots__ = ("component_id",)
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    component_id: int
    def __init__(self, component_id: _Optional[int] = ...) -> None: ...

class ComponentDetailResponse(_message.Message):
    __slots__ = ("component", "available_analogs")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_ANALOGS_FIELD_NUMBER: _ClassVar[int]
    component: ComponentNode
    available_analogs: _containers.RepeatedCompositeFieldContainer[AnalogOption]
    def __init__(self, component: _Optional[_Union[ComponentNode, _Mapping]] = ..., available_analogs: _Optional[_Iterable[_Union[AnalogOption, _Mapping]]] = ...) -> None: ...

class AnalogOption(_message.Message):
    __slots__ = ("analog_id", "name", "manufacturer", "country_code", "unit_cost_rub", "redesign_cost_rub", "lead_time_days", "compatibility_score", "description")
    ANALOG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_COST_RUB_FIELD_NUMBER: _ClassVar[int]
    REDESIGN_COST_RUB_FIELD_NUMBER: _ClassVar[int]
    LEAD_TIME_DAYS_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    analog_id: int
    name: str
    manufacturer: str
    country_code: str
    unit_cost_rub: float
    redesign_cost_rub: float
    lead_time_days: int
    compatibility_score: float
    description: str
    def __init__(self, analog_id: _Optional[int] = ..., name: _Optional[str] = ..., manufacturer: _Optional[str] = ..., country_code: _Optional[str] = ..., unit_cost_rub: _Optional[float] = ..., redesign_cost_rub: _Optional[float] = ..., lead_time_days: _Optional[int] = ..., compatibility_score: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class SimulateAnalogRequest(_message.Message):
    __slots__ = ("component_id", "analog_id")
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    ANALOG_ID_FIELD_NUMBER: _ClassVar[int]
    component_id: int
    analog_id: int
    def __init__(self, component_id: _Optional[int] = ..., analog_id: _Optional[int] = ...) -> None: ...

class SimulateAnalogResponse(_message.Message):
    __slots__ = ("success", "component_id", "old_cfi", "new_cfi", "new_defacto_localization_pct", "cost_delta_rub", "redesign_investment_rub", "implementation_days", "commentary")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    OLD_CFI_FIELD_NUMBER: _ClassVar[int]
    NEW_CFI_FIELD_NUMBER: _ClassVar[int]
    NEW_DEFACTO_LOCALIZATION_PCT_FIELD_NUMBER: _ClassVar[int]
    COST_DELTA_RUB_FIELD_NUMBER: _ClassVar[int]
    REDESIGN_INVESTMENT_RUB_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    COMMENTARY_FIELD_NUMBER: _ClassVar[int]
    success: bool
    component_id: int
    old_cfi: float
    new_cfi: float
    new_defacto_localization_pct: float
    cost_delta_rub: float
    redesign_investment_rub: float
    implementation_days: int
    commentary: str
    def __init__(self, success: bool = ..., component_id: _Optional[int] = ..., old_cfi: _Optional[float] = ..., new_cfi: _Optional[float] = ..., new_defacto_localization_pct: _Optional[float] = ..., cost_delta_rub: _Optional[float] = ..., redesign_investment_rub: _Optional[float] = ..., implementation_days: _Optional[int] = ..., commentary: _Optional[str] = ...) -> None: ...

class UpsertComponentRequest(_message.Message):
    __slots__ = ("product_id", "component")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    component: ComponentNode
    def __init__(self, product_id: _Optional[int] = ..., component: _Optional[_Union[ComponentNode, _Mapping]] = ...) -> None: ...

class UpsertComponentResponse(_message.Message):
    __slots__ = ("success", "component_id", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    component_id: int
    message: str
    def __init__(self, success: bool = ..., component_id: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
