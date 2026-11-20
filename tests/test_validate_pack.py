import datetime as dt
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "domain-scout" / "scripts"))

import validate_pack  # noqa: E402

PACKS = sorted(p for p in (ROOT / "domains").iterdir() if p.is_dir())
SAMPLE = ROOT / "domains" / "creative-direction-film"
TODAY = dt.date(2026, 11, 20)


class PackTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.pack = self.tmp / SAMPLE.name
        shutil.copytree(SAMPLE, self.pack)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit(self, rel, old, new):
        path = self.pack / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture text not found in {rel}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def errors(self, today=TODAY):
        return validate_pack.validate(self.pack, today).errors

    def assertError(self, fragment):
        errs = self.errors()
        self.assertTrue(any(fragment in e for e in errs), f"no error containing {fragment!r}: {errs}")


class TestCommittedPacks(unittest.TestCase):
    def test_every_pack_is_valid(self):
        self.assertTrue(PACKS, "no packs in domains/")
        for pack in PACKS:
            with self.subTest(pack=pack.name):
                r = validate_pack.validate(pack)
                self.assertEqual(r.errors, [])

    def test_template_has_every_file(self):
        template = ROOT / "skills" / "domain-scout" / "templates" / "pack"
        for rel in ["DOMAIN.md", "sources.md", *validate_pack.REFERENCE_FILES]:
            self.assertTrue((template / rel).is_file(), rel)


class TestRules(PackTestCase):
    def test_sample_passes(self):
        self.assertEqual(self.errors(), [])

    def test_name_must_match_folder(self):
        self.edit("DOMAIN.md", "name: creative-direction-film", "name: something-else")
        self.assertError("does not match folder")

    def test_status_values(self):
        self.edit("DOMAIN.md", "status: draft", "status: done")
        self.assertError("status must be")

    def test_reviewed_needs_date(self):
        self.edit("DOMAIN.md", "status: draft", "status: reviewed")
        self.assertError("needs a 'reviewed")

    def test_stale_pack_warns(self):
        r = validate_pack.validate(self.pack, TODAY + dt.timedelta(days=400))
        self.assertTrue(any("refresh" in w for w in r.warnings))

    def test_missing_section(self):
        self.edit("DOMAIN.md", "## Vocabulary", "## Words")
        self.assertError("missing sections: Vocabulary")

    def test_domain_links_references(self):
        self.edit("DOMAIN.md", "(references/tools.md)", "(tools.md)")
        self.assertError("does not link to references/tools.md")

    def test_domain_size_limit(self):
        self.edit("DOMAIN.md", "## Scope", "## Scope\n" + "filler\n" * 200)
        self.assertError("limit is 200")

    def test_question_needs_recommendation(self):
        self.edit("references/questions.md", "Recommended: one stage per system", "One stage per system")
        self.assertError("has no 'Recommended:'")

    def test_question_headings_are_branches(self):
        self.edit("references/questions.md", "## Outcome", "## Goals")
        self.assertError("is not a design-tree branch")

    def test_tool_table_header(self):
        self.edit("references/tools.md", "| Tool | Used for | Integration | Auth | Checked |",
                  "| Tool | Used for | Integration | Auth |")
        self.assertError("table header must be")

    def test_tool_needs_checked(self):
        self.edit("references/tools.md", "| OAuth | registry 2026-11-20 |", "| OAuth | |")
        self.assertError("no Checked value")

    def test_references_do_not_link_each_other(self):
        self.edit("references/patterns.md", "## Teams", "## Teams\n\nSee [tools](tools.md).")
        self.assertError("never link to other files")

    def test_patterns_sections(self):
        self.edit("references/patterns.md", "## Anti-patterns", "## Pitfalls")
        self.assertError("missing section '## Anti-patterns'")

    def test_minimum_sources(self):
        (self.pack / "sources.md").write_text("# Sources\n\nchecked: 2026-11-20\n\n- https://a.example\n")
        self.assertError("need at least 8")

    def test_sources_checked_line(self):
        self.edit("sources.md", "checked: 2026-11-20", "updated recently")
        self.assertError("checked: YYYY-MM-DD")

    def test_literal_secret(self):
        self.edit("references/tools.md", "`${ELEVENLABS_API_KEY}`", "sk-abcdefghijklmnopqrstuvwxyz123456")
        self.assertError("literal credential")


class TestOverlay(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.dir = self.tmp / "creative-direction-film"
        self.dir.mkdir()
        template = ROOT / "skills" / "domain-scout" / "templates" / "overlay" / "OVERLAY.md"
        text = template.read_text(encoding="utf-8")
        text = text.replace("extends: field-focus", "extends: creative-direction-film")
        self.path = self.dir / "OVERLAY.md"
        self.path.write_text(text.replace("YYYY-MM-DD", "2026-11-20"), encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def errors(self):
        return validate_pack.validate(self.dir, TODAY).errors

    def test_template_overlay_passes(self):
        self.assertEqual(self.errors(), [])

    def test_extends_must_match_folder(self):
        self.path.write_text(self.path.read_text().replace("extends: creative-direction-film", "extends: other"))
        self.assertTrue(any("does not match folder" in e for e in self.errors()))

    def test_unknown_section(self):
        self.path.write_text(self.path.read_text() + "\n## Budget\n\n- 10k\n")
        self.assertTrue(any("'Budget' is not one of" in e for e in self.errors()))

    def test_secret_in_overlay(self):
        self.path.write_text(self.path.read_text() + "\n- token ghp_abcdefghijklmnopqrstuvwxyz\n")
        self.assertTrue(any("literal credential" in e for e in self.errors()))


class TestCli(PackTestCase):
    def test_exit_codes(self):
        self.assertEqual(validate_pack.main([str(self.pack)]), 0)
        self.edit("DOMAIN.md", "## Roles", "## People")
        self.assertEqual(validate_pack.main([str(self.pack)]), 1)


if __name__ == "__main__":
    unittest.main()
