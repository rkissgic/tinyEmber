"""Tests for tinyEmber.cli"""

from tinyEmber.cli import _process


def test_process_basic():
    result = _process("hello\nworld", {})
    assert "hello" in result
    assert "world" in result


def test_process_uppercase():
    result = _process("hello", {"uppercase": True})
    assert "HELLO" in result


def test_process_trim():
    result = _process("  hello  ", {"trim": True})
    assert "hello" in result