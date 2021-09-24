"""
OSQuery process_namespaces ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class ProcessNamespaces(BaseModel):
    """
    Linux namespaces for processes running on the host system.
    Examples:
        select * from process_namespaces where pid = 1
    """
    # Process (or thread) ID
    pid = IntegerField()  # {'index': True}
    # cgroup namespace inode
    cgroup_namespace = TextField()
    # ipc namespace inode
    ipc_namespace = TextField()
    # mnt namespace inode
    mnt_namespace = TextField()
    # net namespace inode
    net_namespace = TextField()
    # pid namespace inode
    pid_namespace = TextField()
    # user namespace inode
    user_namespace = TextField()
    # uts namespace inode
    uts_namespace = TextField()

    class Meta:
        table_name = "process_namespaces"
