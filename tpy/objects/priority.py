# This file is part of the TPy TargetProcess API Wrapper.
# Copyright (C) 2012 Jonathan Enzinna
#
# TPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TPy.  If not, see <http://www.gnu.org/licenses/>.

from tpy.objects import TargetProcessEntity
from tpy.objects import entitytype

class Priority(TargetProcessEntity):
    """Object representing the priority of a story, bug or feature"""
    singular = 'Priority'
    plural   = 'Priorities'
    
    fields = {
            "Id"            : TargetProcessField(type='id'),
            "Name"          : TargetProcessField(type=str),
            "Importance"    : TargetProcessField(type=int),
            "IsDefault"     : TargetProcessField(type=bool),
            "EntityType"    : TargetProcessField(type='link',obj=EntityType)
    }   