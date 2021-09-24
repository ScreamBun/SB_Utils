"""
OSQuery wmi_script_event_consumers ORM
"""
from osquery_orm.orm import BaseModel
from peewee import TextField


class WmiScriptEventConsumers(BaseModel):
    """
    WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.
    Examples:
        select filter,consumer,query,scripting_engine,script_file_name,script_text,wsec.name from wmi_script_event_consumers wsec left outer join wmi_filter_consumer_binding wcb on consumer = wsec.relative_path left outer join wmi_event_filters wef on wef.relative_path = wcb.filter;
    """
    # Unique identifier for the event consumer. 
    name = TextField()
    # Name of the scripting engine to use, for example, 'VBScript'. This property cannot be NULL.
    scripting_engine = TextField()
    # Name of the file from which the script text is read, intended as an alternative to specifying the text of the script in the ScriptText property.
    script_file_name = TextField()
    # Text of the script that is expressed in a language known to the scripting engine. This property must be NULL if the ScriptFileName property is not NULL.
    script_text = TextField()
    # The name of the class.
    class_ = TextField(column_name="class")
    # Relative path to the class or instance.
    relative_path = TextField()

    class Meta:
        table_name = "wmi_script_event_consumers"
