# Service dependency

Ayaneo3 Fans talks to `/run/ay3-fancontrol/control.sock` using protocol 1. The
canonical request/response contract is maintained by the service repository:

https://github.com/sknowledge1/Ayaneo-3-Fan-Controls/blob/main/docs/PROTOCOL.md

Before configuration, the Python proxy requests status and validates the protocol.
Compatible v0.4 responses without an explicit version are treated as protocol 1.
Explicit future versions or malformed legacy responses are rejected without
sending the configuration operation.
