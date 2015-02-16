# This file is part of Indico.
# Copyright (C) 2002 - 2015 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import re

from wtforms.fields.core import BooleanField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

from indico.web.forms.base import IndicoForm
from indico.util.i18n import _
from indico.web.forms.fields import PrincipalField, IndicoPasswordField

ROOM_NAME_RE = re.compile(r'[\w\-]+')


class VCRoomForm(IndicoForm):
    name = StringField(_('Name'), [DataRequired(), Length(min=3, max=60), Regexp(ROOM_NAME_RE)],
                       description=_('The name of the room'))
    description = TextAreaField(_('Description'), [DataRequired()], description=_('The description of the room'))
    moderator = PrincipalField(_('Moderator'), multiple=False, description=_('The moderator of the room'))
    auto_mute = BooleanField(_('Auto mute'),
                             description=_('The VidyoDesktop clients will join the meeting muted by default '
                                           '(audio and video)'))
    moderator_pin = IndicoPasswordField(_('Moderator PIN'), toggle=True, description=_('Used to moderate the VC Room'))
    room_pin = IndicoPasswordField(_('Room PIN'), toggle=True,
                                   description=_('Used to protect the access to the VC Room '
                                                 '(leave blank for open access)'))
