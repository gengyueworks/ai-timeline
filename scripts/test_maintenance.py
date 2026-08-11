#!/usr/bin/env python3
"""Small, network-free regression tests for maintenance helpers."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate = load_module("validate-public-data.py", "validate_public_data")
links = load_module("check-source-links.py", "check_source_links")


class MaintenanceTests(unittest.TestCase):
    def test_date_range_is_derived_from_event_dates(self):
        events = [{"date": "1936"}, {"date": "2026-08-06"}, {"date": "1956-06"}]
        self.assertEqual(validate.derive_date_range(events), "1936–2026-08-06")

    def test_full_collection_count_comes_from_events_not_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "full.json"
            path.write_text(json.dumps({"total_events": 272, "events": [{"id": str(i)} for i in range(272)]}), encoding="utf-8")
            self.assertEqual(validate.read_full_collection_count(path), 272)

    def test_network_errors_are_uncertain_not_dead(self):
        self.assertEqual(links.classify_result("timeout"), "network-error")
        self.assertEqual(links.classify_result("ssl"), "network-error")
        self.assertEqual(links.classify_result("reset"), "network-error")

    def test_http_statuses_are_split_by_review_risk(self):
        self.assertEqual(links.classify_http_status(200), "healthy")
        self.assertEqual(links.classify_http_status(403), "blocked")
        self.assertEqual(links.classify_http_status(429), "blocked")
        self.assertEqual(links.classify_http_status(503), "transient")
        self.assertEqual(links.classify_http_status(404), "candidate-dead")
        self.assertEqual(links.classify_http_status(410), "candidate-dead")

    def test_dead_link_needs_two_maintenance_runs_to_be_confirmed(self):
        first = links.add_persistence({"classification": "candidate-dead"}, {})
        second = links.add_persistence({"classification": "candidate-dead"}, first)
        self.assertFalse(first["confirmed_dead"])
        self.assertTrue(second["confirmed_dead"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
