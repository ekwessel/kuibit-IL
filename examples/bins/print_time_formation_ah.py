#!/usr/bin/env python3

# Copyright (C) 2021 Gabriele Bozzola
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/>.

import logging
import os

from kuibit.simdir import SimDir
from kuibit import argparse_helper as pah

"""This script prints the time at which the given horizon was first found.
"""

if __name__ == "__main__":

    desc = __doc__

    parser = pah.init_argparse(desc)
    pah.add_figure_to_parser(parser)

    parser.add_argument(
        "-a",
        "--horizon",
        type=int,
        required=True,
        help="Apparent horizons index",
    )

    parser.add_argument(
        "--parsable",
        action='store_true',
        help="Just print the number",
    )

    args = pah.get_args(parser)

    # Parse arguments

    logger = logging.getLogger(__name__)

    if args.verbose:
        logging.basicConfig(format="%(asctime)s - %(message)s")
        logger.setLevel(logging.DEBUG)

    sim = SimDir(args.datadir)
    sim_hor = sim.horizons

    logger.debug(
        f"Apparent horizons available: {sim_hor.available_apparent_horizons}"
    )

    if args.horizon not in sim_hor.available_apparent_horizons:
        raise ValueError(f"Apparent horizons {args.horizon} is not available")

    time_found = sim_hor[0, args.horizon].formation_time

    if (args.parsable):
        print(f"{time_found}")
    else:
        print(f"Horizon {args.horizon} was first found at time {time_found}")
