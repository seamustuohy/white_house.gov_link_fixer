#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of whitehouse.gov link fixer, a package that opens the latest archived Presidential White House website a whitehouse.gov link exists within.
# Copyright © 2025 seamus tuohy, <code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

import argparse
import requests
import logging
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)
from urllib.parse import urlparse
from requests.exceptions import ConnectionError
import webbrowser

def main():
    args = parse_arguments()
    set_logging(args.verbose, args.debug)
    cur_url = urlparse(args.url.strip())
    if 'whitehouse.gov' not in cur_url.netloc:
        log.error("URL not a whitehouse.gov url.")
        log.debug(f'URL: {new_url}')
        raise ValueError(f"URL {new_url} not a whitehouse.gov url.")
    try:
        r = requests.head(args.url.strip())
        if r.status_code == 200:
            log.info("This is a working url")
            if args.print_on_found is True:
                print(args.url.strip())
            else:
                webbrowser.open(args.url.strip())
            return
    except ConnectionError:
        pass
    new_url = find_replacement(args.url)
    if new_url is not None:
        log.info(f"Found the archived url {new_url}")
        if args.print_on_found is True:
            print(new_url)
        else:
            webbrowser.open(new_url)
    else:
        log.error("Could not find an archived URL. Sorry....")

def find_replacement(url):
    # https://www.archives.gov/presidential-records/research/archived-white-house-websites
    archive_netlocs = [
        "bidenwhitehouse.archives.gov",
        "trumpwhitehouse.archives.gov",
        "obamawhitehouse.archives.gov",
        "georgewbush-whitehouse.archives.gov",
        "clintonwhitehouse1.archives.gov",
        "clintonwhitehouse2.archives.gov",
        "clintonwhitehouse3.archives.gov",
        "clintonwhitehouse4.archives.gov",
        "clintonwhitehouse5.archives.gov",
        "clintonwhitehouse6.archives.gov"
    ]
    url = urlparse(url)
    for netloc in archive_netlocs:
        _check_url = url._replace(netloc=netloc)
        try:
            r = requests.head(_check_url.geturl())
            if r.status_code == 200:
                return _check_url.geturl()
        except ConnectionError:
            continue

# Command Line Functions below this point

def set_logging(verbose=False, debug=False):
    if debug == True:
        log.setLevel("DEBUG")
    elif verbose == True:
        log.setLevel("INFO")

def parse_arguments():
    parser = argparse.ArgumentParser("Archived WhiteHouse.gov link fixer (WHGLF).")
    parser.add_argument("--verbose", "-v",
                        help="Turn verbosity on",
                        action='store_true')
    parser.add_argument("--debug", "-d",
                        help="Turn debugging on",
                        action='store_true')
    parser.add_argument("--print_on_found", "-p",
                        help="Print the archived url instead of opening it in the browser.",
                        action='store_true',)
    parser.add_argument("--url", "-u",
                        help="whitehouse.gov URL to try find in the archives.")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
