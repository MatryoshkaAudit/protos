import grpc
from protos.bom import bom_service_pb2, bom_service_pb2_grpc
from protos.bom.dto import (
    GetBOMTreeResponseDTO,
    ComponentNodeDTO,
    SimulateAnalogResponseDTO,
)


def _proto_node_to_dto(node) -> ComponentNodeDTO:
    return ComponentNodeDTO(
        id=node.id,
        name=node.name,
        article=node.article,
        tier=node.tier,
        country_code=node.country_code,
        manufacturer=node.manufacturer,
        hs_code=node.hs_code,
        cost_rub=node.cost_rub,
        quantity=node.quantity,
        criticality=node.criticality,
        country_risk=node.country_risk,
        analog_availability=node.analog_availability,
        cfi_score=node.cfi_score,
        is_chokepoint=node.is_chokepoint,
        parent_id=node.parent_id if node.parent_id != 0 else None,
        children=[_proto_node_to_dto(c) for c in node.children],
        notes=node.notes,
    )


class BOMClient:
    """Высокоуровневый клиент взаимодействия с BOM Service по gRPC"""

    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = bom_service_pb2_grpc.BOMServiceStub(self.channel)

    async def get_bom_tree(self, product_id: int, include_analogs: bool = True) -> GetBOMTreeResponseDTO:
        request = bom_service_pb2.GetBOMTreeRequest(
            product_id=product_id,
            include_analogs=include_analogs,
        )
        response = await self.stub.GetBOMTree(request)
        return GetBOMTreeResponseDTO(
            product_id=response.product_id,
            product_name=response.product_name,
            root=_proto_node_to_dto(response.root) if response.HasField("root") else None,
            total_cost_rub=response.total_cost_rub,
            paper_localization_pct=response.paper_localization_pct,
            defacto_localization_pct=response.defacto_localization_pct,
            total_components=response.total_components,
            chokepoints_count=response.chokepoints_count,
            overall_cfi_max=response.overall_cfi_max,
        )

    async def simulate_analog_substitution(
        self, component_id: int, analog_id: int
    ) -> SimulateAnalogResponseDTO:
        request = bom_service_pb2.SimulateAnalogRequest(
            component_id=component_id,
            analog_id=analog_id,
        )
        response = await self.stub.SimulateAnalogSubstitution(request)
        return SimulateAnalogResponseDTO(
            success=response.success,
            component_id=response.component_id,
            old_cfi=response.old_cfi,
            new_cfi=response.new_cfi,
            new_defacto_localization_pct=response.new_defacto_localization_pct,
            cost_delta_rub=response.cost_delta_rub,
            redesign_investment_rub=response.redesign_investment_rub,
            implementation_days=response.implementation_days,
            commentary=response.commentary,
        )

    async def close(self):
        await self.channel.close()
