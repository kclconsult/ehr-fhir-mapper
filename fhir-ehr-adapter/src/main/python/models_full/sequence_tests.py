#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2018-01-16.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import sequence
from .fhirdate import FHIRDate


class SequenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Sequence", js["resourceType"])
        return sequence.Sequence(js)
    
    def testSequence1(self):
        inst = self.instantiate_from("sequence-graphic-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence1(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence1(inst2)
    
    def implSequence1(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "graphic-example-1")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NC_000002.12")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273732)
        self.assertEqual(inst.referenceSeq.windowStart, 128273724)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].cigar, "1M")
        self.assertEqual(inst.variant[0].end, 128273726)
        self.assertEqual(inst.variant[0].observedAllele, "G")
        self.assertEqual(inst.variant[0].referenceAllele, "T")
        self.assertEqual(inst.variant[0].start, 128273725)
    
    def testSequence2(self):
        inst = self.instantiate_from("sequence-example-TPMT-one.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence2(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence2(inst2)
    
    def implSequence2(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(inst.id, "example-TPMT-one")
        self.assertEqual(inst.observedSeq, "T-C-C-C-A-C-C-C")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NT_007592.15")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 18143955)
        self.assertEqual(inst.referenceSeq.windowStart, 18130918)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 18139214)
        self.assertEqual(inst.variant[0].observedAllele, "A")
        self.assertEqual(inst.variant[0].referenceAllele, "G")
        self.assertEqual(inst.variant[0].start, 18139214)
    
    def testSequence3(self):
        inst = self.instantiate_from("sequence-example-pgx-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence3(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence3(inst2)
    
    def implSequence3(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "example-pgx-2")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NG_007726.3")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 55227980)
        self.assertEqual(inst.referenceSeq.windowStart, 55227970)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 55227979)
        self.assertEqual(inst.variant[0].observedAllele, "G")
        self.assertEqual(inst.variant[0].referenceAllele, "T")
        self.assertEqual(inst.variant[0].start, 55227978)
    
    def testSequence4(self):
        inst = self.instantiate_from("sequence-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence4(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence4(inst2)
    
    def implSequence4(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NC_000009.11")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 22125510)
        self.assertEqual(inst.referenceSeq.windowStart, 22125500)
        self.assertEqual(inst.repository[0].name, "GA4GH API")
        self.assertEqual(inst.repository[0].type, "openapi")
        self.assertEqual(inst.repository[0].url, "http://grch37.rest.ensembl.org/ga4gh/variants/3:rs1333049?content-type=application/json")
        self.assertEqual(inst.repository[0].variantsetId, "3:rs1333049")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 22125504)
        self.assertEqual(inst.variant[0].observedAllele, "C")
        self.assertEqual(inst.variant[0].referenceAllele, "G")
        self.assertEqual(inst.variant[0].start, 22125503)
    
    def testSequence5(self):
        inst = self.instantiate_from("sequence-example-fda.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence5(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence5(inst2)
    
    def implSequence5(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(inst.id, "fda-example")
        self.assertEqual(inst.quality[0].end, 101770080)
        self.assertEqual(inst.quality[0].fScore, 0.545551)
        self.assertEqual(inst.quality[0].gtFP, 2186)
        self.assertEqual(inst.quality[0].method.coding[0].code, "job-ByxYPx809jFVy21KJG74Jg3Y")
        self.assertEqual(inst.quality[0].method.coding[0].system, "https://precision.fda.gov/jobs/")
        self.assertEqual(inst.quality[0].method.text, "Vcfeval + Hap.py Comparison")
        self.assertEqual(inst.quality[0].precision, 0.428005)
        self.assertEqual(inst.quality[0].queryFP, 10670)
        self.assertEqual(inst.quality[0].queryTP, 7984)
        self.assertEqual(inst.quality[0].recall, 0.752111)
        self.assertEqual(inst.quality[0].standardSequence.coding[0].code, "file-Bk50V4Q0qVb65P0v2VPbfYPZ")
        self.assertEqual(inst.quality[0].standardSequence.coding[0].system, "https://precision.fda.gov/files/")
        self.assertEqual(inst.quality[0].start, 10453)
        self.assertEqual(inst.quality[0].truthFN, 2554)
        self.assertEqual(inst.quality[0].truthTP, 7749)
        self.assertEqual(inst.quality[0].type, "SNP")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NC_000001.11")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 101770080)
        self.assertEqual(inst.referenceSeq.windowStart, 10453)
        self.assertEqual(inst.repository[0].name, "FDA")
        self.assertEqual(inst.repository[0].type, "login")
        self.assertEqual(inst.repository[0].url, "https://precision.fda.gov/files/file-Bx37ZK009P4bX5g3qjkFZV38")
        self.assertEqual(inst.repository[0].variantsetId, "file-Bx37ZK009P4bX5g3qjkFZV38")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 13117)
        self.assertEqual(inst.variant[0].observedAllele, "T")
        self.assertEqual(inst.variant[0].referenceAllele, "G")
        self.assertEqual(inst.variant[0].start, 13116)
    
    def testSequence6(self):
        inst = self.instantiate_from("coord-1base-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence6(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence6(inst2)
    
    def implSequence6(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(inst.id, "coord-1-base")
        self.assertEqual(inst.observedSeq, "ACATGGTAGC")
        self.assertEqual(inst.referenceSeq.referenceSeqString, "ACGTAGTC")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 8)
        self.assertEqual(inst.referenceSeq.windowStart, 1)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].cigar, "3I")
        self.assertEqual(inst.variant[0].end, 3)
        self.assertEqual(inst.variant[0].observedAllele, "ATG")
        self.assertEqual(inst.variant[0].referenceAllele, "-")
        self.assertEqual(inst.variant[0].start, 2)
        self.assertEqual(inst.variant[1].cigar, "3I")
        self.assertEqual(inst.variant[1].end, 5)
        self.assertEqual(inst.variant[1].observedAllele, "T")
        self.assertEqual(inst.variant[1].referenceAllele, "A")
        self.assertEqual(inst.variant[1].start, 5)
        self.assertEqual(inst.variant[2].cigar, "1D")
        self.assertEqual(inst.variant[2].end, 7)
        self.assertEqual(inst.variant[2].observedAllele, "-")
        self.assertEqual(inst.variant[2].referenceAllele, "T")
        self.assertEqual(inst.variant[2].start, 7)
    
    def testSequence7(self):
        inst = self.instantiate_from("sequence-graphic-example-4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence7(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence7(inst2)
    
    def implSequence7(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "graphic-example-4")
        self.assertEqual(inst.referenceSeq.chromosome.coding[0].code, "2")
        self.assertEqual(inst.referenceSeq.chromosome.coding[0].display, "chromosome 2")
        self.assertEqual(inst.referenceSeq.chromosome.coding[0].system, "http://hl7.org/fhir/ValueSet/chromosome-human")
        self.assertEqual(inst.referenceSeq.genomeBuild, "GRCh 38")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273740)
        self.assertEqual(inst.referenceSeq.windowStart, 128273736)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
    
    def testSequence8(self):
        inst = self.instantiate_from("sequence-graphic-example-5.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence8(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence8(inst2)
    
    def implSequence8(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "graphic-example-5")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NC_000002.12")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 128273736)
        self.assertEqual(inst.referenceSeq.windowStart, 128273732)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
    
    def testSequence9(self):
        inst = self.instantiate_from("sequence-example-TPMT-two.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence9(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence9(inst2)
    
    def implSequence9(self, inst):
        self.assertEqual(inst.coordinateSystem, 1)
        self.assertEqual(inst.id, "example-TPMT-two")
        self.assertEqual(inst.observedSeq, "T-C-T-C-G-C-C-C")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NT_007592.15")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 18143955)
        self.assertEqual(inst.referenceSeq.windowStart, 18130918)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 18131012)
        self.assertEqual(inst.variant[0].observedAllele, "T")
        self.assertEqual(inst.variant[0].referenceAllele, "C")
        self.assertEqual(inst.variant[0].start, 18131012)
    
    def testSequence10(self):
        inst = self.instantiate_from("sequence-example-pgx-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence10(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence10(inst2)
    
    def implSequence10(self, inst):
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "example-pgx-1")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NG_007726.3")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 55227980)
        self.assertEqual(inst.referenceSeq.windowStart, 55227970)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 55227977)
        self.assertEqual(inst.variant[0].observedAllele, "G")
        self.assertEqual(inst.variant[0].referenceAllele, "T")
        self.assertEqual(inst.variant[0].start, 55227976)

