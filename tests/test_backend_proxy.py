import asyncio
import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main


CONFIG = {"mode": "quiet", "percent": 15, "curve": [10, 30, 40, 70, 100]}


class ProtocolTests(unittest.TestCase):
    def response(self, **changes):
        return {"ok": True, "api_version": 1, "version": "0.5.0",
                "config": copy.deepcopy(CONFIG), **changes}

    def test_current_protocol_is_accepted(self):
        result = main.normalize_response(self.response())
        self.assertTrue(result["ok"])
        self.assertEqual(result["api_version"], 1)

    def test_compatible_v04_response_is_normalized(self):
        legacy = self.response()
        legacy.pop("api_version")
        result = main.normalize_response(legacy)
        self.assertTrue(result["ok"])
        self.assertEqual(result["api_version"], 1)

    def test_future_and_malformed_responses_are_rejected(self):
        for response in [self.response(api_version=2), {"ok": True, "config": {}}]:
            with self.subTest(response=response):
                self.assertFalse(main.normalize_response(response)["ok"])

    def test_incompatible_preflight_never_sends_configuration(self):
        with patch.object(main, "exchange", return_value={"ok": False, "error": "Unsupported"}) as exchange:
            result = asyncio.run(main.Plugin().set_config(CONFIG))
        self.assertFalse(result["ok"])
        exchange.assert_called_once_with("status")

    def test_compatible_preflight_sends_configuration(self):
        with patch.object(main, "exchange", side_effect=[self.response(), self.response()]) as exchange:
            result = asyncio.run(main.Plugin().set_config(CONFIG))
        self.assertTrue(result["ok"])
        self.assertEqual(exchange.call_args_list[1].args, ("configure", CONFIG))


if __name__ == "__main__":
    unittest.main()
