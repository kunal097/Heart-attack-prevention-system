from channels.routing import route
from .consumers import ws_receive,ws_connect,ws_disconnect

channel_routing = [
    route("websocket.receive",ws_receive,path=r"^/dashboard/"),
    route("websocket.connect",ws_connect,path=r"^/dashboard/"),
    route("websocket.disconnect",ws_disconnect,path=r"^/dashboard/"),
]