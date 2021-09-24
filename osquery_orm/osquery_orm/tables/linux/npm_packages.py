"""
OSQuery npm_packages ORM
"""
import platform as pfm
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class NpmPackages(BaseModel):
    """
    Lists all npm packages in a directory or globally installed in a system.
    Examples:
        select * from npm_packages
        select * from npm_packages where directory = '/home/user/my_project'
    """
    # Package display name
    name = TextField()
    # Package supplied version
    version = TextField()
    # Package supplied description
    description = TextField()
    # Package author name
    author = TextField()
    # License for package
    license = TextField()
    # Module's package.json path
    path = TextField()
    # Node module's directory where this package is located
    directory = TextField()  # {'index': True}

    class Meta:
        table_name = "npm_packages"


# OS specific properties for Linux
class Linux_NpmPackages(NpmPackages):
    # Pids that contain a namespace
    pid_with_namespace = IntegerField()  # {'additional': True, 'hidden': True}
    # Mount namespace id
    mount_namespace_id = TextField()  # {'hidden': True}
