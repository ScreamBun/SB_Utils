"""
OSQuery cups_jobs ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, TextField


class CupsJobs(BaseModel):
    """
    Returns all completed print jobs from cups.
    """
    # Title of the printed job
    title = TextField()
    # The printer the job was sent to
    destination = TextField()
    # The user who printed the job
    user = TextField()
    # The format of the print job
    format = TextField()
    # The size of the print job
    size = IntegerField()
    # When the job completed printing
    completed_time = IntegerField()
    # How long the job took to process
    processing_time = IntegerField()
    # When the print request was initiated
    creation_time = IntegerField()

    class Meta:
        table_name = "cups_jobs"
