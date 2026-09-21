import asyncio
import json
import socket

API_VERSION = 1
SOCKET = "/run/ay3-fancontrol/control.sock"


def normalize_response(response):
    if not isinstance(response, dict):
        return {"ok": False, "error": "The fan service returned an invalid response."}
    if not response.get("ok"):
        return response
    reported = response.get("api_version")
    if reported is None:
        # v0.4 did not identify the protocol. Accept only its known response shape.
        config = response.get("config")
        if not isinstance(config, dict) or not {"mode", "percent", "curve"}.issubset(config):
            return {"ok": False, "error": "The fan service response is not compatible with protocol 1."}
        reported = API_VERSION
    if type(reported) is not int or reported != API_VERSION:
        return {"ok": False, "error": "Unsupported fan-service protocol. Update Ayaneo3 Fans and the shared service together."}
    normalized = dict(response)
    normalized["api_version"] = API_VERSION
    return normalized


def exchange(operation, config=None):
    message = {"operation": operation}
    if config is not None:
        message["config"] = config
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.settimeout(3)
            client.connect(SOCKET)
            client.sendall(json.dumps(message).encode() + b"\n")
            return normalize_response(json.loads(client.makefile("rb").readline(16384)))
    except Exception as error:
        return {"ok": False, "error": "Fan service unavailable: " + str(error)}


class Plugin:
    async def _main(self):
        pass

    async def _unload(self):
        # The supervised service owns the loop; menu/plugin reloads do not interrupt it.
        pass

    async def get_status(self):
        return await asyncio.to_thread(exchange, "status")

    async def set_config(self, config: dict):
        # Check compatibility before sending a request that can write hardware.
        status = await asyncio.to_thread(exchange, "status")
        if not status.get("ok"):
            return status
        return await asyncio.to_thread(exchange, "configure", config)
