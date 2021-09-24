"""
OSQuery prometheus_metrics ORM
"""
from osquery_orm.orm import BaseModel
from peewee import DoubleField, BigIntegerField, TextField


class PrometheusMetrics(BaseModel):
    """
    Retrieve metrics from a Prometheus server.
    """
    # Address of prometheus target
    target_name = TextField()
    # Name of collected Prometheus metric
    metric_name = TextField()
    # Value of collected Prometheus metric
    metric_value = DoubleField()
    # Unix timestamp of collected data in MS
    timestamp_ms = BigIntegerField()

    class Meta:
        table_name = "prometheus_metrics"
