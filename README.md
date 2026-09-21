# Ayaneo3 Fans

Fan controls for every AYANEO 3 model in Decky Loader. Ayaneo3 Fans is a thin
frontend for the separately installed shared fan service maintained at:
https://github.com/sknowledge1/Ayaneo-3-Fan-Controls

This repository contains only the Decky plugin. It does not contain or install
native OpenGamepadUI code, systemd units, kernel drivers, or privileged fan code.

## Features

- Firmware automatic, manual, custom-curve, and Quiet modes.
- Live RPM, CPU temperature, effective duty, and controller faults.
- 0% fan stop while cool and the service's tested 10% running floor.
- Shared saved settings with the native OGUI frontend when both are installed.
- Protocol checks before any configuration request.

## Install

1. Install or update the shared service from
   [AYANEO 3 Fan Controls](https://github.com/sknowledge1/Ayaneo-3-Fan-Controls).
2. In Decky Settings, enable **Developer Mode**.
3. Open **Developer → Install Plugin from URL** and paste:

   ```text
   https://github.com/sknowledge1/Ayaneo3-Fans/releases/latest/download/Ayaneo3-Fans.zip
   ```

4. Confirm installation, then open **Decky → Ayaneo3 Fans**.

See the [complete installation and migration guide](docs/INSTALL.md).

The archive keeps the internal directory `ay3-fancontrol/` so it replaces older
manual installations safely even though the visible name is Ayaneo3 Fans.

## Compatibility

Ayaneo3 Fans protocol 1 supports:

- service v0.5 and newer protocol-1 responses;
- compatible legacy v0.4 responses that omitted `api_version`.

Unknown or malformed protocols are rejected before a configuration write. The
plugin shows an upgrade message instead of attempting hardware changes.

All AYANEO 3 CPU variants are eligible in the service. Physical validation is on
the 8840U model; other CPU-name paths have simulated coverage.

## Build and test

```sh
pnpm install --frozen-lockfile --ignore-scripts
pnpm build
pnpm test
python3 scripts/build-decky-package.py
```

The project uses pnpm 9.15.9. The readable pinned `@decky/api` source and its LGPL
license are included under `vendor/`.

## Project status

This is a manually distributed community plugin. It is not submitted to or
approved by the official Decky store. See [store status](docs/STORE_STATUS.md).

The code includes Codex assistance and discloses that provenance. Project code is
MIT licensed; bundled Decky API code retains its LGPL license.

Previous combined releases through v0.4.0 remain at
https://github.com/sknowledge1/Ayaneo-3-Fan-Controls/releases/tag/v0.4.0.
