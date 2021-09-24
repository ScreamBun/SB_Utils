"""
OSQuery wmi_filter_consumer_binding ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class WmiFilterConsumerBinding(BaseModel):
    """
    Lists the relationship between event consumers and filters.
    Examples:
        select * from wmi_filter_consumer_binding
    """
    # Reference to an instance of __EventConsumer that represents the object path to a logical consumer, the recipient of an event.
    consumer = TextField()
    # Reference to an instance of __EventFilter that represents the object path to an event filter which is a query that specifies the type of event to be received.
    filter = TextField()
    # The name of the class.
    class_ = TextField(column_name="class")
    # Relative path to the class or instance.
    relative_path = TextField()

    class Meta:
        table_name = "wmi_filter_consumer_binding"
