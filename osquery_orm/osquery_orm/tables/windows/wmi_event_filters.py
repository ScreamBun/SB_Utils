"""
OSQuery wmi_event_filters ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class WmiEventFilters(BaseModel):
    """
    Lists WMI event filters.
    Examples:
        select * from wmi_event_filters
    """
    # Unique identifier of an event filter.
    name = TextField()
    # Windows Management Instrumentation Query Language (WQL) event query that specifies the set of events for consumer notification, and the specific conditions for notification.
    query = TextField()
    # Query language that the query is written in.
    query_language = TextField()
    # The name of the class.
    class_ = TextField(column_name="class")
    # Relative path to the class or instance.
    relative_path = TextField()

    class Meta:
        table_name = "wmi_event_filters"
