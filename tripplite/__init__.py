"""
Python driver for TrippLite UPS battery backups.

Distributed under the GNU General Public License v2
Copyright (C) 2018 NuMat Technologies
"""
from tripplite.driver import Battery, list_devices


def command_line():
    """Command line tool exposed through package install."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Read TrippLite status.")
    parser.add_argument('-l', '--list', action='store_true',
                        help="List all devices and their product ids")
    parser.add_argument('-p', '--product_id', type=int, default=None,
                        help="The TrippLite UPS HID product id. Only needed "
                        "if multiple TrippLite devices are connected.")
    args = parser.parse_args()

    if args.list:
        for name, product_id in list_devices():
            print("0x%04x %s" % (product_id, name or "Unknown"))
        return

    with Battery(args.product_id) as battery:
        print(json.dumps(battery.get(), indent=4, sort_keys=True))


if __name__ == '__main__':
    command_line()
