import json
from pathlib import Path


def test_roster_contract():
    root = Path(__file__).resolve().parents[1]
    source = (root / 'autoloads' / 'RosterDataService.gd').read_text(encoding='utf-8')

    required_markers = [
        'same_element_bonus',
        'validate_champion',
        'passives',
        'team_synergy_theme',
        'base_stats',
        'skills',
    ]

    missing = [marker for marker in required_markers if marker not in source]
    assert not missing, f'Missing generator contract markers: {missing}'


def test_element_catalog_has_internal_synergy():
    root = Path(__file__).resolve().parents[1]
    elements = (root / 'data' / 'elements.json').read_text(encoding='utf-8')
    assert 'internal_synergy' in elements
    assert 'team_synergy_theme' in elements
    assert 'signature_gameplay' in elements


def test_generated_champion_has_full_runtime_profile():
    root = Path(__file__).resolve().parents[1]
    source = (root / 'autoloads' / 'RosterDataService.gd').read_text(encoding='utf-8')
    assert 'base_stats' in source
    assert 'skills' in source
    assert 'build_skill_set' in source
    assert 'range(1, 11)' in source


def test_generated_champion_has_ten_skills():
    root = Path(__file__).resolve().parents[1]
    source = (root / 'autoloads' / 'RosterDataService.gd').read_text(encoding='utf-8')
    assert 'range(1, 11)' in source
    assert 'size() < 10' in source


def test_generated_roster_counts_are_consistent():
    root = Path(__file__).resolve().parents[1]
    roster = json.loads((root / 'data' / 'generated_roster.json').read_text(encoding='utf-8'))
    assert len(roster['monolithes']) == 216
    assert len(roster['hybrids']) == 66
    assert roster['stats']['overall_total'] == 282


if __name__ == '__main__':
    import json
    test_roster_contract()
    test_element_catalog_has_internal_synergy()
    test_generated_champion_has_full_runtime_profile()
    test_generated_champion_has_ten_skills()
    test_generated_roster_counts_are_consistent()
    print('roster_contract_ok')
