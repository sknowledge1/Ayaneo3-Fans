# Install Ayaneo3 Fans

## 1. Install the shared service

Download the latest native/service bundle from
https://github.com/sknowledge1/Ayaneo-3-Fan-Controls/releases/latest, extract it,
and run from that directory in Bazzite Desktop Mode:

```sh
sudo python3 scripts/install-device.py . --user "$USER" --backend-only
```

Verify it before installing the frontend:

```sh
systemctl is-active ay3-fancontrol.service
python3 /var/lib/ay3-fancontrol/app/ay3_fancontrol.py --status
```

The service should be active and report `ok: true`. A v0.5 service also reports
`api_version: 1`.

## 2. Install the Decky plugin

1. Return to Gaming Mode and open the Steam Quick Access Menu.
2. Open Decky with its plug icon, then open Decky Settings.
3. Under General, enable Developer Mode.
4. Open Developer → Install Plugin from URL.
5. Paste and install:

   ```text
   https://github.com/sknowledge1/Ayaneo3-Fans/releases/latest/download/Ayaneo3-Fans.zip
   ```

Alternatively, download `Ayaneo3-Fans.zip` from the latest release and choose
Developer → Install Plugin from ZIP File.

## 3. Use it

Open Decky → Ayaneo3 Fans, select Automatic, Manual, Custom curve, or Quiet, and
choose Apply changes. Restore automatic control returns ownership to firmware.

## Updating from the combined v0.4.0 release

1. Install native/service v0.5.0 first. Its installer preserves the Decky files
   and detaches them from native installer ownership.
2. Install the v0.5.0 Ayaneo3-Fans ZIP or URL over the existing plugin.
3. Confirm that Quiet/custom settings and live telemetry remain present.

The internal folder remains `~/homebrew/plugins/ay3-fancontrol`. Future removal
or updates are performed through Decky Loader. Removing the Decky plugin does not
remove the service or native OGUI frontend.

## Troubleshooting

- **Service unavailable:** install/start the shared service and check
  `sudo journalctl -u ay3-fancontrol.service -b`.
- **Protocol error:** update the shared service and Ayaneo3 Fans together.
- **Plugin missing:** check Decky Settings → Plugins for hidden/disabled status.
- **Native menu wanted:** follow the native repository's OGUI installation guide.
