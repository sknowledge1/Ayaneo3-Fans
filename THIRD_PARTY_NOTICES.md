# Third-party notices

`vendor/decky-api-1.1.3` contains the official `@decky/api` 1.1.3 source distributed
by Steam Deck Homebrew under its LGPL license. The original license is retained
both there and in `LICENSE.decky-api`.

The build script injects this plugin's manifest, removes the empty types re-export,
and combines the API source with the readable frontend. Original source is included
so the dependency remains inspectable and replaceable.

The privileged AYANEO fan service and kernel driver are separate dependencies and
are not bundled in this project. Ayaneo3 Fans communicates only through the
documented local service protocol.
