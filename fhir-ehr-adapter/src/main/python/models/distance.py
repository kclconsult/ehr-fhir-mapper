#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/Distance) on 2018-01-16.
#  2018, SMART Health IT.


from . import quantity

class Distance(quantity.Quantity):
    """ A length - a value with a unit that is a physical distance.
    """
    
    resource_type = "Distance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Distance, self).__init__(jsondict=jsondict, strict=strict)


