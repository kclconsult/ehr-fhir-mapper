#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2018-01-16.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import capabilitystatement
from .fhirdate import FHIRDate


class CapabilityStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CapabilityStatement", js["resourceType"])
        return capabilitystatement.CapabilityStatement(js)
    
    def testCapabilityStatement1(self):
        inst = self.instantiate_from("capabilitystatement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement instance")
        self.implCapabilityStatement1(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement1(inst2)
    
    def implCapabilityStatement1(self, inst):
        self.assertEqual(inst.acceptUnknown, "both")
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "wile@acme.org")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description, "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertEqual(inst.document[0].documentation, "Basic rules for all documents in the EHR system")
        self.assertEqual(inst.document[0].mode, "consumer")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.fhirVersion, "1.0.0")
        self.assertEqual(inst.format[0], "xml")
        self.assertEqual(inst.format[1], "json")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.implementation.description, "main EHR at ACME")
        self.assertEqual(inst.implementation.url, "http://10.2.3.4/fhir")
        self.assertEqual(inst.kind, "instance")
        self.assertEqual(inst.messaging[0].documentation, "ADT A08 equivalent for external system notifications")
        self.assertEqual(inst.messaging[0].endpoint[0].address, "mllp:10.1.1.10:9234")
        self.assertEqual(inst.messaging[0].endpoint[0].protocol.code, "mllp")
        self.assertEqual(inst.messaging[0].endpoint[0].protocol.system, "http://hl7.org/fhir/message-transport")
        self.assertEqual(inst.messaging[0].event[0].category, "Consequence")
        self.assertEqual(inst.messaging[0].event[0].code.code, "admin-notify")
        self.assertEqual(inst.messaging[0].event[0].code.system, "http://hl7.org/fhir/message-type")
        self.assertEqual(inst.messaging[0].event[0].documentation, "Notification of an update to a patient resource. changing the links is not supported")
        self.assertEqual(inst.messaging[0].event[0].focus, "Patient")
        self.assertEqual(inst.messaging[0].event[0].mode, "receiver")
        self.assertEqual(inst.messaging[0].reliableCache, 30)
        self.assertEqual(inst.name, "ACME EHR capability statement")
        self.assertEqual(inst.publisher, "ACME Corporation")
        self.assertEqual(inst.purpose, "Main EHR capability statement, published for contracting and operational support")
        self.assertEqual(inst.rest[0].compartment[0], "http://hl7.org/fhir/compartment/Patient")
        self.assertEqual(inst.rest[0].documentation, "Main FHIR endpoint for acem health")
        self.assertEqual(inst.rest[0].interaction[0].code, "transaction")
        self.assertEqual(inst.rest[0].interaction[1].code, "history-system")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertTrue(inst.rest[0].resource[0].conditionalCreate)
        self.assertEqual(inst.rest[0].resource[0].conditionalDelete, "not-supported")
        self.assertFalse(inst.rest[0].resource[0].conditionalUpdate)
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "vread")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "Only supported for patient records since 12-Dec 2012")
        self.assertEqual(inst.rest[0].resource[0].interaction[2].code, "update")
        self.assertEqual(inst.rest[0].resource[0].interaction[3].code, "history-instance")
        self.assertEqual(inst.rest[0].resource[0].interaction[4].code, "create")
        self.assertEqual(inst.rest[0].resource[0].interaction[5].code, "history-type")
        self.assertTrue(inst.rest[0].resource[0].readHistory)
        self.assertEqual(inst.rest[0].resource[0].searchInclude[0], "Organization")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].definition, "http://hl7.org/fhir/SearchParameter/Patient-identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].documentation, "Only supports search by institution MRN")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].name, "identifier")
        self.assertEqual(inst.rest[0].resource[0].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].definition, "http://hl7.org/fhir/SearchParameter/Patient-careprovider")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].name, "careprovider")
        self.assertEqual(inst.rest[0].resource[0].searchParam[1].type, "reference")
        self.assertEqual(inst.rest[0].resource[0].searchRevInclude[0], "Person")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertFalse(inst.rest[0].resource[0].updateCreate)
        self.assertEqual(inst.rest[0].resource[0].versioning, "versioned-update")
        self.assertEqual(inst.rest[0].security.certificate[0].blob, "IHRoaXMgYmxvYiBpcyBub3QgdmFsaWQ=")
        self.assertEqual(inst.rest[0].security.certificate[0].type, "application/jwt")
        self.assertTrue(inst.rest[0].security.cors)
        self.assertEqual(inst.rest[0].security.description, "See Smart on FHIR documentation")
        self.assertEqual(inst.rest[0].security.service[0].coding[0].code, "SMART-on-FHIR")
        self.assertEqual(inst.rest[0].security.service[0].coding[0].system, "http://hl7.org/fhir/restful-security-service")
        self.assertEqual(inst.software.name, "EHR")
        self.assertEqual(inst.software.releaseDate.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.software.releaseDate.as_json(), "2012-01-04")
        self.assertEqual(inst.software.version, "0.00.020.2134")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.version, "20130510")
    
    def testCapabilityStatement2(self):
        inst = self.instantiate_from("capabilitystatement-phr-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CapabilityStatement instance")
        self.implCapabilityStatement2(inst)
        
        js = inst.as_json()
        self.assertEqual("CapabilityStatement", js["resourceType"])
        inst2 = capabilitystatement.CapabilityStatement(js)
        self.implCapabilityStatement2(inst2)
    
    def implCapabilityStatement2(self, inst):
        self.assertEqual(inst.acceptUnknown, "no")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-06-18").date)
        self.assertEqual(inst.date.as_json(), "2013-06-18")
        self.assertEqual(inst.description, "Prototype Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.fhirVersion, "1.0.0")
        self.assertEqual(inst.format[0], "json")
        self.assertEqual(inst.format[1], "xml")
        self.assertEqual(inst.id, "phr")
        self.assertEqual(inst.kind, "capability")
        self.assertEqual(inst.name, "PHR Template")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.rest[0].documentation, "Protoype server Capability Statement for September 2013 Connectathon")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "When a client searches patients with no search criteria, they get a list of all patients they have access too. Servers may elect to offer additional search parameters, but this is not required")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.rest[0].resource[1].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[1].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].documentation, "_id parameter always supported. For the connectathon, servers may elect which search parameters are supported")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[1].type, "DocumentReference")
        self.assertEqual(inst.rest[0].resource[2].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[2].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[2].type, "Condition")
        self.assertEqual(inst.rest[0].resource[3].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[3].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].documentation, "which diagnostic discipline/department created the report")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].name, "service")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].type, "token")
        self.assertEqual(inst.rest[0].resource[3].type, "DiagnosticReport")
        self.assertEqual(inst.rest[0].security.service[0].text, "OAuth")
        self.assertEqual(inst.software.name, "ACME PHR Server")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

