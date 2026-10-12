"""Heading anchors must match the IDs Hugo generates (double hyphens kept)."""

from tools.sync.wikilinks import convert_wikilinks, heading_anchor_slug, slugify


def test_em_dash_heading_keeps_double_hyphen() -> None:
    assert (
        heading_anchor_slug("Motor Descending — Alien Hand Syndrome")
        == "motor-descending--alien-hand-syndrome"
    )


def test_slash_and_quotes_heading() -> None:
    assert (
        heading_anchor_slug('The "Can Move / Won\'t Move" Distinction')
        == "the-can-move--wont-move-distinction"
    )


def test_plain_heading_unchanged() -> None:
    assert heading_anchor_slug("The Marker Bridge") == "the-marker-bridge"


def test_page_slugify_still_collapses() -> None:
    slug = slugify("Motor Descending — Alien Hand Syndrome")
    assert slug == "motor-descending-alien-hand-syndrome"


def test_wikilink_anchor_uses_heading_slug() -> None:
    out = convert_wikilinks(
        "[[neurological-dissociations-as-interface-architecture"
        "#Motor Descending — Alien Hand Syndrome|x]]",
        link_resolver=lambda t: "/topics/neurological-dissociations-as-interface-architecture/",
    )
    assert "#motor-descending--alien-hand-syndrome)" in out
