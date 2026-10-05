# MatryoshkaAudit / Protos

Центральный репозиторий Protocol Buffers контрактов, скомпилированных gRPC-стабов и Pydantic DTO для экосистемы **MatryoshkaAudit**.

## Структура пакета

```
protos/
├── bom/         # Управление многоуровневым деревом изделий (Tier 0-3), O-Ring метрики
├── policy/      # Нормативный аудит ПП РФ № 719, де-факто локализация, ИИ-сценарии
└── audit/       # Неизменяемый журнал аудита, цифровые заключения Минпромторга
```

## Генерация стабов

```bash
python -m grpc_tools.protoc \
  -I protos \
  --python_out=protos \
  --grpc_python_out=protos \
  --pyi_out=protos \
  protos/bom/bom_service.proto \
  protos/policy/policy_service.proto \
  protos/audit/audit_service.proto
```

## Установка пакета локально

```bash
pip install -e .
```
