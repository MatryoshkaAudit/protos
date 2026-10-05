import grpc
from protos.audit import audit_service_pb2, audit_service_pb2_grpc
from protos.audit.dto import (
    WriteAuditEventResponseDTO,
    QueryAuditTrailResponseDTO,
    AuditRecordDTO,
    IssueCertificateResponseDTO,
)


class AuditClient:
    """Высокоуровневый клиент взаимодействия с Audit Service по gRPC"""

    def __init__(self, host: str = "localhost", port: int = 50053):
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = audit_service_pb2_grpc.AuditServiceStub(self.channel)

    async def log_event(
        self,
        event_type: str,
        actor_id: int,
        actor_role: str,
        resource_type: str,
        resource_id: int,
        details_json: str = "{}",
        ip_address: str = "127.0.0.1",
    ) -> WriteAuditEventResponseDTO:
        request = audit_service_pb2.WriteAuditEventRequest(
            event_type=event_type,
            actor_id=actor_id,
            actor_role=actor_role,
            resource_type=resource_type,
            resource_id=resource_id,
            details_json=details_json,
            ip_address=ip_address,
        )
        response = await self.stub.WriteAuditEvent(request)
        return WriteAuditEventResponseDTO(
            success=response.success,
            audit_id=response.audit_id,
            hash_sha256=response.hash_sha256,
            recorded_at=response.recorded_at,
        )

    async def query_trail(
        self,
        resource_type: str,
        resource_id: int,
        limit: int = 50,
        offset: int = 0,
    ) -> QueryAuditTrailResponseDTO:
        request = audit_service_pb2.QueryAuditTrailRequest(
            resource_type=resource_type,
            resource_id=resource_id,
            limit=limit,
            offset=offset,
        )
        response = await self.stub.QueryAuditTrail(request)
        return QueryAuditTrailResponseDTO(
            records=[
                AuditRecordDTO(
                    id=r.id,
                    event_type=r.event_type,
                    actor_id=r.actor_id,
                    actor_role=r.actor_role,
                    resource_type=r.resource_type,
                    resource_id=r.resource_id,
                    details_json=r.details_json,
                    recorded_at=r.recorded_at,
                    hash_sha256=r.hash_sha256,
                )
                for r in response.records
            ],
            total_count=response.total_count,
        )

    async def issue_certificate(
        self,
        product_id: int,
        certificate_type: str = "PP_719_ORIGIN",
        valid_months: int = 12,
        certified_by: str = "Минпромторг РФ",
    ) -> IssueCertificateResponseDTO:
        request = audit_service_pb2.IssueCertificateRequest(
            product_id=product_id,
            certificate_type=certificate_type,
            valid_months=valid_months,
            certified_by=certified_by,
        )
        response = await self.stub.IssueCertificate(request)
        return IssueCertificateResponseDTO(
            is_issued=response.is_issued,
            certificate_number=response.certificate_number,
            qr_verification_url=response.qr_verification_url,
            issued_at=response.issued_at,
            expires_at=response.expires_at,
            certified_defacto_loc=response.certified_defacto_loc,
            certified_points=response.certified_points,
            digital_signature_hash=response.digital_signature_hash,
        )

    async def close(self):
        await self.channel.close()
