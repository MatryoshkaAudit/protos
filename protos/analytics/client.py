import grpc
from protos.analytics import analytics_service_pb2, analytics_service_pb2_grpc
from protos.analytics.dto import (
    AuditLedgerEventDTO,
    RecordEventResponseDTO,
    MonteCarloSimulationResponseDTO,
    MonteCarloIterationDTO,
    AnalyticsSummaryDTO,
    TimeSeriesDataPointDTO,
)


class AsyncAnalyticsServiceClient:
    """Асинхронный клиент для взаимодействия с Analytics & ClickHouse OLAP Service"""

    def __init__(self, target: str = "localhost:50053"):
        self.target = target
        self._channel = None
        self._stub = None

    async def connect(self):
        self._channel = grpc.aio.insecure_channel(self.target)
        self._stub = analytics_service_pb2_grpc.AnalyticsServiceStub(self._channel)

    async def close(self):
        if self._channel:
            await self._channel.close()

    async def record_event(self, event_dto: AuditLedgerEventDTO) -> RecordEventResponseDTO:
        if not self._stub:
            await self.connect()

        event_msg = analytics_service_pb2.AuditEventMessage(
            event_id=event_dto.event_id,
            timestamp=event_dto.timestamp,
            trace_id=event_dto.trace_id,
            product_id=event_dto.product_id,
            product_name=event_dto.product_name,
            event_type=event_dto.event_type,
            actor_type=event_dto.actor_type,
            paper_localization_pct=event_dto.paper_localization_pct,
            defacto_localization_pct=event_dto.defacto_localization_pct,
            vulnerability_gap_pct=event_dto.vulnerability_gap_pct,
            chokepoints_count=event_dto.chokepoints_count,
            digital_signature=event_dto.digital_signature,
            payload_json=event_dto.payload_json,
        )

        req = analytics_service_pb2.RecordEventRequest(event=event_msg)
        resp = await self._stub.RecordEvent(req)
        return RecordEventResponseDTO(
            success=resp.success,
            event_id=resp.event_id,
            message=resp.message,
        )

    async def run_monte_carlo(
        self, product_id: int, iterations_count: int = 1000, blocked_countries: list[str] | None = None
    ) -> MonteCarloSimulationResponseDTO:
        if not self._stub:
            await self.connect()

        req = analytics_service_pb2.RunMonteCarloRequest(
            product_id=product_id,
            iterations_count=iterations_count,
            blocked_countries=blocked_countries or [],
        )
        resp = await self._stub.RunMonteCarlo(req)
        samples = [
            MonteCarloIterationDTO(
                iteration=s.iteration,
                is_paralyzed=s.is_paralyzed,
                days_to_halt=s.days_to_halt,
                loss_rub=s.loss_rub,
                failed_chokepoint=s.failed_chokepoint,
            )
            for s in resp.sample_iterations
        ]
        return MonteCarloSimulationResponseDTO(
            run_id=resp.run_id,
            product_id=resp.product_id,
            total_iterations=resp.total_iterations,
            paralysis_probability_pct=resp.paralysis_probability_pct,
            median_days_to_halt=resp.median_days_to_halt,
            value_at_risk_rub=resp.value_at_risk_rub,
            sample_iterations=samples,
            executive_summary=resp.executive_summary,
        )

    async def get_analytics_summary(self, product_id: int) -> AnalyticsSummaryDTO:
        if not self._stub:
            await self.connect()

        req = analytics_service_pb2.GetAnalyticsSummaryRequest(product_id=product_id)
        resp = await self._stub.GetAnalyticsSummary(req)
        trend = [
            TimeSeriesDataPointDTO(
                timestamp=t.timestamp,
                paper_localization_pct=t.paper_localization_pct,
                defacto_localization_pct=t.defacto_localization_pct,
            )
            for t in resp.localization_trend
        ]
        return AnalyticsSummaryDTO(
            product_id=resp.product_id,
            total_events_recorded=resp.total_events_recorded,
            current_vulnerability_gap_pct=resp.current_vulnerability_gap_pct,
            active_chokepoints_count=resp.active_chokepoints_count,
            localization_trend=trend,
            storage_engine=resp.storage_engine,
        )
