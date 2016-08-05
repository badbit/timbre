# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('timbre')

from timbre_lib import Window
from timbre.AboutTimbreDialog import AboutTimbreDialog
from timbre.PreferencesTimbreDialog import PreferencesTimbreDialog

# See timbre_lib.Window.py for more details about how this class works
class TimbreWindow(Window):
    __gtype_name__ = "TimbreWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(TimbreWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutTimbreDialog
        self.PreferencesDialog = PreferencesTimbreDialog

        # Code for other initialization actions should be added here.

