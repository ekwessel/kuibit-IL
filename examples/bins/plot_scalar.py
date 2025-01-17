#!/usr/bin/env python3

# Copyright (C) 2020-2021 Gabriele Bozzola
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

import matplotlib.pyplot as plt

from kuibit.simdir import SimDir
from kuibit import argparse_helper as pah
from kuibit.visualize_matplotlib import setup_matplotlib, save


"""This script plots a timeseries with options specified via command-line.
"""

if __name__ == "__main__":
    setup_matplotlib()

    desc = "Plot a given timeseries."

    parser = pah.init_argparse(desc)
    pah.add_figure_to_parser(parser)

    parser.add_argument(
        "--variable", type=str, required=True, help="Variable to plot."
    )
    parser.add_argument(
        "--reduction",
        type=str,
        choices=[
            "scalar",
            "minimum",
            "maximum",
            "norm1",
            "norm2",
            "average",
            "infnorm",
        ],
        default="scalar",
        help="Reduction to plot.",
    )
    parser.add(
        "--logxaxis", help="Use a logarithmic x axis.", action="store_true"
    )
    parser.add(
        "--logyaxis", help="Use a logarithmic y axis.", action="store_true"
    )
    args = pah.get_args(parser)

    if args.reduction == "scalar":
        ext = ""
        red = ""
    else:
        ext = "_"
        red = args.reduction

    if args.figname is None:
        figname = f"{args.variable}{ext}{red}"
    else:
        figname = args.figname

    logger = logging.getLogger(__name__)

    if args.verbose:
        logging.basicConfig(format="%(asctime)s - %(message)s")
        logger.setLevel(logging.DEBUG)

    logger.debug(f"Reading variable {args.variable}")
    sim = SimDir(args.datadir)
    reader = sim.timeseries[args.reduction]
    logger.debug(f"Available variables {reader}")
    var = reader[args.variable]
    logger.debug(f"Read variable {args.variable}")

    logger.debug("Plotting timeseries")
    plt.plot(var)
    if args.logxaxis:
        plt.xscale("log")
    if args.logyaxis:
        plt.yscale("log")

    plt.grid(which="major", linewidth="0.7")
    plt.grid(which="minor", linewidth="0.2")
    plt.xlabel("t")
    plt.ylabel(f"{red} {args.variable}")

    output_path = os.path.join(args.outdir, figname)
    logger.debug(f"Saving in {output_path}")
    save(output_path, args.fig_extension, as_tikz=args.as_tikz)
