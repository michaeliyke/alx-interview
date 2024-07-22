#!/usr/bin/python3
"""Log stats Module"""


import sys
import signal
import time
import os
import re
from typing import List


def print_logs(stats: dict, total_size: int) -> None:
    """Print logs from stats and total_size"""
    print("File size: {:d}".format(total_size))
    for key, value in sorted(stats.items()):
        # print only if value is not 0
        if value:
            print("{:s}: {:d}".format(key, value))


def signal_handler(sig, frame) -> None:
    """Signal handler"""
    print_logs(stats, total_size)


def get_size(line: str) -> int:
    """Get size from line"""
    # Use rsplit below to split from right by the first space only
    # So only two elements are returned, the rest, and size
    try:
        size = line.rsplit(' ', 1)[1]
    except Exception:
        size = ""
    return int(size) if size.isdigit() else 0


def parse_line(line: str) -> List[str]:
    """Parse line to get status code"""
    # Use rsplit to split the line into three parts,
    # the rest, status code, and size
    return line.rsplit(' ', 2)


def update_stats(stats: dict, line: List[str]) -> None:
    """Update stats with status code"""
    if len(line) > 2:
        key = line[-2]
        if key in stats:
            stats[key] += 1


if __name__ == '__main__':
    stats = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
    total_size = 0
    count = 0
    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            try:
                line = input()
                count += 1
                total_size += get_size(line)
                update_stats(stats, parse_line(line))
                if count == 10:
                    print_logs(stats, total_size)
                    count = 0
            except EOFError:
                print_logs(stats, total_size)
                # Flush output buffer
                sys.stdout.flush()
                break
    except KeyboardInterrupt:
        print_logs(stats, total_size)
        # Flush output buffer
        sys.stdout.flush()
        raise KeyboardInterrupt
