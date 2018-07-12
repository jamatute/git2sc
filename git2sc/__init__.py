#!/usr/bin/python
# git2sc: program to sync a git documentation repository to Confluence.
#
# Copyright (C) 2018 jamatute <jamatute@paradigmadigital.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
from git2sc.git2sc import Git2SC
from git2sc.cli import load_parser


def main():
    parser = load_parser()
    args = parser.parse_args()
    try:
        api_url = os.environ['GIT2SC_API_URL']
    except KeyError:
        print('GIT2SC_API_URL environmental variable not set')
        return

    try:
        auth = os.environ['GIT2SC_AUTH']
    except KeyError:
        print('GIT2SC_AUTH environmental variable not set')
        return

    g = Git2SC(api_url, auth)

    if args.subcommand == 'article':
        g.update_page(args.article_id, args.content)


if __name__ == "__main__":
    main()