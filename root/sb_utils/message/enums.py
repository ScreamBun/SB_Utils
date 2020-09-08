from enum import Enum


class MessageType(Enum):
    """
    The type of an OpenC2 Message
    """
    Command = 'cmd'         # The initiator of a two-way message exchange.
    Response = 'rsp'        # A response linked to a request in a two-way message exchange.
    Notification = 'notif'  # A (one-way) message that is not a request or response.  (Placeholder)
