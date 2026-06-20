"""Regression tests for the largest corpus source module."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CODEX_TEXT = (ROOT / "metalaws" / "codex-v1.md").read_text(encoding="utf-8")
CROSS_REFERENCE_TEXT = (ROOT / "metalaws" / "cross-references.md").read_text(
    encoding="utf-8"
)


def declared_law_ids(text):
    return re.findall(r"\[([A-FL][0-9]+)\]", text)


def law_sort_key(law_id):
    return law_id[0], int(law_id[1:])


class MetaLawsCodexTest(unittest.TestCase):
    def test_seed_law_id_grid_is_complete(self):
        ids_by_family = {family: set() for family in "LABCDEF"}
        for law_id in declared_law_ids(CODEX_TEXT):
            match = re.fullmatch(r"([A-FL])([0-9]+)", law_id)
            if match:
                ids_by_family[match.group(1)].add(int(match.group(2)))

        for family, numbers in ids_by_family.items():
            with self.subTest(family=family):
                missing_numbers = set(range(1, 8)) - numbers
                self.assertEqual(missing_numbers, set())

    def test_comprehensive_catalog_keeps_all_nine_domains_in_order(self):
        catalog = CODEX_TEXT.split(
            "Universal Laws, Principles, and Axioms: A Cross-Domain Codex", 1
        )[1]
        expected_sections = [
            (1, "Natural Sciences"),
            (2, "Mathematics and Logic"),
            (3, "Philosophy"),
            (4, "Symbolic Systems"),
            (5, "Social and Behavioral Sciences"),
            (6, "Spiritual and Esoteric Systems"),
            (7, "Legal and Political Systems"),
            (8, "Artistic and Cultural Rules"),
            (9, "Game Design and Worldbuilding"),
        ]

        positions = []
        for number, title in expected_sections:
            marker = f"{number}. {title}"
            with self.subTest(marker=marker):
                self.assertIn(marker, catalog)
            positions.append(catalog.index(marker))

        self.assertEqual(positions, sorted(positions))

    def test_recurring_meta_patterns_are_present(self):
        section = CODEX_TEXT.split("Recurring Meta-Patterns Across Domains", 1)[1]
        pattern_titles = re.findall(r"\s*\u2022\s*([^:\n]+):", section)

        self.assertEqual(
            pattern_titles,
            [
                "Duality and Balance",
                "Cause and Effect (Causality)",
                "Recursion and Self-Similarity",
                "Entropy and Decay vs. Order and Growth",
                "Emergence and Complexity from Simplicity",
                "Human-Centered Patterns",
                "Systems of Governance in Systems",
            ],
        )

    def test_cross_reference_ids_are_declared_and_summarized(self):
        codex_ids = set(declared_law_ids(CODEX_TEXT))
        section_ids = re.findall(
            r"^## ([A-FL][0-9]+): .+$", CROSS_REFERENCE_TEXT, flags=re.MULTILINE
        )
        summary_ids = re.findall(
            r"^\| ([A-FL][0-9]+)\b", CROSS_REFERENCE_TEXT, flags=re.MULTILINE
        )

        self.assertEqual(section_ids, summary_ids)
        missing_ids = sorted(set(section_ids) - codex_ids, key=law_sort_key)
        self.assertEqual(missing_ids, [])

    def test_cross_reference_sections_have_multiple_tradition_mappings(self):
        sections = re.split(r"(?m)^## ", CROSS_REFERENCE_TEXT)
        for section in sections[1:]:
            if section.startswith("Cross-Reference Summary"):
                continue

            header = section.splitlines()[0]
            mappings = re.findall(r"^- \*\*[^*]+:\*\*", section, flags=re.MULTILINE)
            with self.subTest(section=header):
                self.assertGreaterEqual(len(mappings), 3)


if __name__ == "__main__":
    unittest.main()
