# Test case for the BLAST+ number of alignments limit "issue".

This git repository contains a small test case to reproduce the
["-max_taget_seqs issue"](https://gist.github.com/sujaikumar/504b3b7024eaf3a04ef5)
found by [Sujai Kumar](https://github.com/sujaikumar) in December 2015.

The files ``tests/older_matches.*`` contain a small protein BLAST database
based on a subset of the NCBI NR database as of 2018-06-08 matching the
tardigrade query sequence in Sujai's original report.

My 2015 blog post ["What BLAST's max-target-sequences doesn't do"
](http://blastedbio.blogspot.co.uk/2015/12/blast-max-target-sequences-bug.html)
gave a reasonable summary of the situation at the time, with quotes
from the NCBI BLAST developers explaining this was a feature not a bug.

My 2015 blog post was cited in this recent paper:

    Shah et al. (2018)
    Misunderstood parameter of NCBI BLAST impacts the correctness of bioinformatics workflows.
    https://doi.org/10.1093/bioinformatics/bty833

My follow up blog post [BLAST max alignment limits repartee - part
one](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-repartee-one.html)
introduces the small self-contained test case in this repository, and
emphasises that this issue is not specific to ``-max_target_seqs`` but also
affects the limits ``-num_descriptions`` and ``-num_alignments`` used with the
human readable plain text or HTML output.

[BLAST max alignment limits repartee - part
two](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-repartee-two.html)
explored the effect of database order (I could not reproduce the problem
described in Shah et al. 2018), and the internal *N\*2+50* alignment limit.

Nidhi Shah then got in touch via the blog comments to say that the
[Shah et al (2018) test case is now on
GitHub](https://github.com/shahnidhi/BLAST_maxtargetseq_analysis).
