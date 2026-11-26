#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — prints one fortune cookie line.

The line is a warm, rueful joke on a liquidation: the market took the
coins and the sleep, but the trader's talent for buying the top survives.
"""
LINE = "Fear not, trader: the market took your coins and your sleep, but never your talent for buying the top."


def get_line():
    """Return the fortune cookie line."""
    return LINE


if __name__ == "__main__":
    print(get_line())
