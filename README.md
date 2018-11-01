# Test case for the BLAST+ number of alignments limit "issue".

This git repository contains a small test case to reproduce for the
["-max_taget_seqs issue"](https://gist.github.com/sujaikumar/504b3b7024eaf3a04ef5)
found by [Sujai Kumar](https://github.com/sujaikumar) in Dec 2015.

The files ``tests/older_matches.*`` contain a small protein BLAST database
based on a subset of the NCBI NR database as of 2018-06-08 matching the
tardigrade query sequence in Sujai's original report.

My 2015 blog post ["What BLAST's max-target-sequences doesn't do"
](http://blastedbio.blogspot.co.uk/2015/12/blast-max-target-sequences-bug.html)
gave a reasonable summary of the situation at the time, with quotes
from the NCBI BLAST developers explaining this was a feature not a bug.

Further blog posts are planned to discuss the claims in this recent paper:

    Shah et al. (2018)
    Misunderstood parameter of NCBI BLAST impacts the correctness of bioinformatics workflows.
    https://doi.org/10.1093/bioinformatics/bty833
