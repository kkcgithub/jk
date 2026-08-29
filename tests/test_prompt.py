import pytest

from noir_app.noir.prompt import build_noir_prompt


def test_build_noir_prompt_includes_description_and_style():
    prompt = build_noir_prompt("a detective in a trench coat")
    assert "a detective in a trench coat" in prompt
    assert "film noir" in prompt


def test_build_noir_prompt_rejects_empty_description():
    with pytest.raises(ValueError):
        build_noir_prompt("   ")
