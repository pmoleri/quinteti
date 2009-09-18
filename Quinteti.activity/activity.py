#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#
# Copyright 2008, 2009 Pablo Moleri, ceibalJAM
# This file is part of Quinteti.
#
# Quinteti is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Quinteti is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Quinteti.  If not, see <http://www.gnu.org/licenses/>.

"""Quinteti Activity main module for Sugar import.

This Activity is based on olpcgames.PyGameActivity.
The activity attributa game_name is the module name that
has the main() function."""

from sugar.activity.activity import ActivityToolbox
from olpcgames import activity
from gettext import gettext as _

# PyGameActivity: http://www.vrplumber.com/sugar-docs/olpcgames.activity.html
class Quinteti(activity.PyGameActivity):
    """Set up QuinTeTi activity."""
    game_name = 'main'          # Module name with main() function.
    game_title = _('QuinTeTi')
    game_size = None
