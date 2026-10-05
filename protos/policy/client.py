import grpc
from protos.policy import policy_service_pb2, policy_service_pb2_grpc
from protos.policy.dto import (
    EvaluatePP719ResponseDTO,
    PointBreakdownDTO,
    AuditDeFactoResponseDTO,
    ChokepointItemDTO,
    SimulateSanctionsShockResponseDTO,
    GenerateGeopoliticalScenarioResponseDTO,
)


class PolicyClient:
    """Высокоуровневый клиент взаимодействия с Policy Service по gRPC"""

    def __init__(self, host: str = "localhost", port: int = 50052):
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = policy_service_pb2_grpc.PolicyServiceStub(self.channel)

    async def evaluate_pp719(
        self, product_id: int, industry_code: str = "28.3"
    ) -> EvaluatePP719ResponseDTO:
        request = policy_service_pb2.EvaluatePP719Request(
            product_id=product_id,
            industry_code=industry_code,
        )
        response = await self.stub.EvaluatePP719(request)
        return EvaluatePP719ResponseDTO(
            product_id=response.product_id,
            is_compliant=response.is_compliant,
            achieved_points=response.achieved_points,
            required_points=response.required_points,
            ad_valorem_pct=response.ad_valorem_pct,
            required_ad_valorem_pct=response.required_ad_valorem_pct,
            operation_breakdown=[
                PointBreakdownDTO(
                    operation_name=p.operation_name,
                    points_awarded=p.points_awarded,
                    verified=p.verified,
                    evidence_doc=p.evidence_doc,
                )
                for p in response.operation_breakdown
            ],
            status_decision=response.status_decision,
            certificate_recommendation=response.certificate_recommendation,
        )

    async def audit_defacto(
        self, product_id: int, include_chokepoints: bool = True
    ) -> AuditDeFactoResponseDTO:
        request = policy_service_pb2.AuditDeFactoRequest(
            product_id=product_id,
            include_chokepoints=include_chokepoints,
        )
        response = await self.stub.AuditDeFactoLocalization(request)
        return AuditDeFactoResponseDTO(
            product_id=response.product_id,
            paper_localization_pct=response.paper_localization_pct,
            defacto_localization_pct=response.defacto_localization_pct,
            vulnerability_gap_pct=response.vulnerability_gap_pct,
            critical_chokepoints_found=response.critical_chokepoints_found,
            chokepoints=[
                ChokepointItemDTO(
                    component_id=c.component_id,
                    component_name=c.component_name,
                    tier=c.tier,
                    country=c.country,
                    cost_rub=c.cost_rub,
                    cfi_score=c.cfi_score,
                    risk_reason=c.risk_reason,
                    potential_paralysis_scope=c.potential_paralysis_scope,
                )
                for c in response.chokepoints
            ],
            o_ring_summary=response.o_ring_summary,
        )

    async def simulate_shock(
        self,
        product_id: int,
        blocked_countries: list[str],
        blocked_categories: list[str],
        enforce_secondary: bool = True,
    ) -> SimulateSanctionsShockResponseDTO:
        request = policy_service_pb2.SimulateSanctionsShockRequest(
            product_id=product_id,
            blocked_countries=blocked_countries,
            blocked_categories=blocked_categories,
            enforce_secondary_sanctions=enforce_secondary,
        )
        response = await self.stub.SimulateSanctionsShock(request)
        return SimulateSanctionsShockResponseDTO(
            product_id=response.product_id,
            shock_name=response.shock_name,
            production_paralysis_risk_pct=response.production_paralysis_risk_pct,
            blocked_components_count=response.blocked_components_count,
            blocked_value_rub=response.blocked_value_rub,
            blocked_items=[
                ChokepointItemDTO(
                    component_id=c.component_id,
                    component_name=c.component_name,
                    tier=c.tier,
                    country=c.country,
                    cost_rub=c.cost_rub,
                    cfi_score=c.cfi_score,
                    risk_reason=c.risk_reason,
                    potential_paralysis_scope=c.potential_paralysis_scope,
                )
                for c in response.blocked_items
            ],
            estimated_days_until_stockout=response.estimated_days_until_stockout,
            mitigation_roadmap=response.mitigation_roadmap,
        )

    async def generate_geopolitical_scenario(
        self, event_description: str, target_industry: str = "Лесозаготовительная техника", product_id: int = 1
    ) -> GenerateGeopoliticalScenarioResponseDTO:
        request = policy_service_pb2.GenerateGeopoliticalScenarioRequest(
            event_description=event_description,
            target_industry=target_industry,
            product_id=product_id,
        )
        response = await self.stub.GenerateGeopoliticalScenario(request)
        return GenerateGeopoliticalScenarioResponseDTO(
            scenario_id=response.scenario_id,
            scenario_title=response.scenario_title,
            ai_executive_summary=response.ai_executive_summary,
            dynamic_policy_json=response.dynamic_policy_json,
            calculated_impact_severity=response.calculated_impact_severity,
            affected_supply_chains=list(response.affected_supply_chains),
            recommended_urgent_actions=list(response.recommended_urgent_actions),
        )

    async def close(self):
        await self.channel.close()
