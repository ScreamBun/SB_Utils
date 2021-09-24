"""
OSQuery video_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField, BigIntegerField, TextField


class VideoInfo(BaseModel):
    """
    Retrieve video card information of the machine.
    """
    # The amount of bits per pixel to represent color.
    color_depth = IntegerField()
    # The driver of the device.
    driver = TextField()
    # The date listed on the installed driver.
    driver_date = BigIntegerField()
    # The version of the installed driver.
    driver_version = TextField()
    # The manufacturer of the gpu.
    manufacturer = TextField()
    # The model of the gpu.
    model = TextField()
    # The series of the gpu.
    series = TextField()
    # The current resolution of the display.
    video_mode = TextField()

    class Meta:
        table_name = "video_info"
