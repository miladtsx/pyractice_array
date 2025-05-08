import pytest
from rotate_group_words.rotate_group_words import (
    is_similar, rotate_word, rotate_word_once, iterating_through_input, rotate_group_words
)

# --- Unit tests ---
def test_is_similar_true():
    assert is_similar("abcd", "cdab")
    assert is_similar("abcd", "dabc")
    assert is_similar("abcd", "bcda")
    assert is_similar("a", "a")
    assert is_similar("", "")

def test_is_similar_false():
    assert not is_similar("abcd", "abce")
    assert not is_similar("abcd", "abc")
    assert not is_similar("abcd", "efgh")
    assert not is_similar("abcd", "")
    assert not is_similar("", "abcd")

def test_rotate_word_once():
    assert rotate_word_once("abcd") == "dabc"
    assert rotate_word_once("a") == "a"
    assert rotate_word_once("") == ""

def test_rotate_word():
    assert rotate_word("abcd", 1) == "dabc"
    assert rotate_word("abcd", 2) == "cdab"
    assert rotate_word("abcd", 4) == "abcd"
    assert rotate_word("a", 3) == "a"
    assert rotate_word("", 5) == ""

def test_iterating_through_input_basic():
    words = ["abcd", "cdab", "dabc", "bcda", "efgh", "ghfe"]
    result = iterating_through_input(words)
    assert set(result.keys()) == {"abcd", "efgh", "ghfe"}
    assert set(result["abcd"]) == {"abcd", "cdab", "dabc", "bcda"}
    assert result["efgh"] == ["efgh"]
    assert result["ghfe"] == ["ghfe"]

def test_iterating_through_input_empty():
    assert iterating_through_input([]) == {}

def test_iterating_through_input_single():
    assert iterating_through_input(["a"]) == {"a": ["a"]}

# --- Integration test for rotate_group_words (captures print output) ---
def test_rotate_group_words_print(monkeypatch):
    words = ["abcd", "cdab", "dabc", "bcda", "efgh", "ghfe"]
    output = []
    monkeypatch.setattr("builtins.print", lambda x: output.append(x))
    rotate_group_words(words)
    assert any("abcd: [abcd, cdab, dabc, bcda]" in line for line in output)
    assert any("efgh: [efgh]" in line for line in output)
    assert any("ghfe: [ghfe]" in line for line in output)

# --- CLI integration test ---
import subprocess
import sys
import os

def test_cli_entry(tmp_path):
    script = os.path.join(os.path.dirname(__file__), "../src/rotate_group_words/entry.py")
    result = subprocess.run(
        [sys.executable, script, "-w", "abcd,cdab,dabc,bcda,efgh,ghfe"],
        capture_output=True, text=True
    )
    assert "abcd: [abcd, cdab, dabc, bcda]" in result.stdout
    assert "efgh: [efgh]" in result.stdout
    assert "ghfe: [ghfe]" in result.stdout
    assert result.returncode == 0
