"""
OSQuery shell_history ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, ForeignKeyField, TextField
from .users import Users


class ShellHistory(BaseModel):
    """
    A line-delimited (command) table of per-user .*_history data.
    Examples:
        select * from users join shell_history using (uid)
    """
    # Shell history owner
    uid = BigIntegerField()  # {'additional': True}
    # Entry timestamp. It could be absent, default value is 0.
    time = IntegerField()
    # Unparsed date/line/command history line
    command = TextField()
    # Path to the .*_history for this user
    history_file = TextField()
    shell_history = ForeignKeyField(Users, backref='uid')

    class Meta:
        table_name = "shell_history"
