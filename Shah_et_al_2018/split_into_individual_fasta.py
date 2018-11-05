#!/usr/bin/env python
"""Script to split multi-record FASTA file into one file per record."""

import sys

from Bio import SeqIO

stem = sys.argv[1]

total = 0
for i, record in enumerate(SeqIO.parse(sys.stdin, "fasta")):
    total += SeqIO.write(record, "%s_%i.fasta" % (stem, i + 1), "fasta")
print("%i done" % total)
