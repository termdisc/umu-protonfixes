"""METAL GEAR SOLID"""

from protonfixes import util


def main() -> None:
    """Override for wrapper shipped with the game"""
    util.winedll_override('ddraw', util.OverrideOrder.NATIVE_BUILTIN)
    util.winedll_override('dinput', util.OverrideOrder.NATIVE_BUILTIN)
