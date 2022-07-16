"""Test for main.py."""

import pytest

from game_of_life import main


def test_main():
    """Test the main function."""
    with pytest.raises(SystemExit):
        main.main()
