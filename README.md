# Test cases for the BLAST+ number of alignments limit "issue".

This git repository contains some small test cases to reproduce the
["-max_taget_seqs issue"](https://gist.github.com/sujaikumar/504b3b7024eaf3a04ef5)
found by [Sujai Kumar](https://github.com/sujaikumar) in December 2015.

## BLASTP example originally from Sujai Kumar (2015)

The files ``Kumar_et_al_2015/older_matches.*`` contain a small protein BLAST
database based on a subset of the NCBI NR database as of 2018-06-08 matching
the tardigrade query sequence in Sujai's original report.

My blog post [BLAST max alignment limits repartee - part
one](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-repartee-one.html)
introduced this test case (see also the longer history below).

## MEGABLAST example originally from Nidhi Shah (2018)

The files under ``Shah_et_al_2018/`` contain a nucleotide BLAST database
(``db.fasta``, ``db_rand_1.fasta``, ``db_rand_2.fasta``) and a FASTA query
file (``example.fasta``), downloaded from the links given on [Nidhi Shah's
repository](https://github.com/shahnidhi/BLAST_maxtargetseq_analysis),
and files I created from them (de-duplicated database files, and single
query FASTA files used in my testing).

My blog post [BLAST max alignment limits reply - part
three](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-part-three.html)
introduced this	test case (see also the longer history below).

## History

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
described in Shah et al. 2018), and the internal *N\*2+50* alignment limit
(applicable to BLASTP - see below).

Nidhi Shah then got in touch via the blog comments to say that the
[Shah et al (2018) test case is now on
GitHub](https://github.com/shahnidhi/BLAST_maxtargetseq_analysis).

[BLAST max alignment limits - part
three](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-part-three.html)
examined the Shah et al (2018) test case, reproduced the strange behaviour,
and demonstrated the benefits of deduplicating the database. See the files under
``Shah_et_al_2018/`` for this.

[BLAST max alignment limits - part
four](https://blastedbio.blogspot.com/2018/11/blast-max-alignment-limits-part-four.html)
examined the source code which sets the internal aligment limit and explains
why with BLASTP and other protein database searches you get a higher internal
alignment limit than with MEGABLAST, BLASTN or other nucleotide database searches.
