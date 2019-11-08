#!/usr/bin/env python
# -*- coding: utf-8 -*
# Copyright: See LICENSE for details.
# Authors: Guannan Ma (@mythmgn),
"""
:description:

"""
from __future__ import print_function
from pyamis import mod


def test_table():
    table = mod.Table(
        title='table example',
        what='abc'
    )
    # table.set_title('A Amis Table Example')
    table.add_column('text', 'measurement', '${mea}')
    table.add_column('text', 'avg value', '${avg_value}')
    table.add_column('text', '90% value', '${percent_90}')
    table.add_column('text', '99% value', '${percent_99}')
    table.add_column('text', '99.9% value', '${percent_999}')
    rows_dict = {
        'mea': 'mb/s',
        'avg_value': 11,
        'percent_90': 11.5,
        'percent_99': 11.54,
        'percent_999': 11.55,
    }
    table.set_rows([rows_dict])
    table.render()

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent

