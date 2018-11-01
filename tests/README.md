This folder contains a small test case to reproduce the
["-max_taget_seqs issue"](https://gist.github.com/sujaikumar/504b3b7024eaf3a04ef5)
found by [Sujai Kumar](https://github.com/sujaikumar) in Dec 2015.

The idea is to capture all the current NR matches to the query, and then
excluding the recent tardigate sequences which were not present back
in December 2015.

# Creating FASTA file older_matches.fasta

Using NR data 2018-06-08 (8 June 2018)

    $ export BLASTDB=/mnt/shared/cluster/blast/ncbi/extracted/
    $ blastp -query input.fasta -db nr -outfmt "6 std sskingdoms sscinames staxids" -max_target_seqs 500 -evalue 1e-5 > out.1e-5.max500.taxids.txt
    $ time blastp -query input.fasta -db nr -outfmt "6 std sskingdoms sscinames staxids" -max_target_seqs 100 -evalue 1e-5 >out.1e-5.max100.taxids.txt

    $ head out.1e-5.max100.taxids.txt
    nHd.2.3.1.t00019-RA	OQV20892.1	100.000	122	0	0	1	122	1	122	4.77e-85	253	Eukaryota	Hypsibius dujardini	232323
    nHd.2.3.1.t00019-RA	GAV08169.1	75.806	124	30	0	1	124	51	174	5.53e-45	162	Eukaryota	Ramazzottius varieornatus	947166
    nHd.2.3.1.t00019-RA	KRX89027.1	63.115	122	45	0	1	122	105	226	7.01e-37	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KRX89025.1	63.115	122	45	0	1	122	105	226	1.43e-36	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KFD69381.1	61.983	121	46	0	1	121	466	586	1.85e-36	141	Eukaryota	Trichuris suis	68888
    nHd.2.3.1.t00019-RA	KRZ17714.1	63.115	122	45	0	1	122	121	242	1.86e-36	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KFD48812.1	61.983	121	46	0	1	121	419	539	1.92e-36	141	Eukaryota	Trichuris suis	68888
    nHd.2.3.1.t00019-RA	KHJ41189.1	61.983	121	46	0	1	121	39	159	1.98e-36	141	Eukaryota	Trichuris suis	68888
    nHd.2.3.1.t00019-RA	KRX89026.1	63.115	122	45	0	1	122	153	274	2.42e-36	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	CDW52156.1	61.983	121	46	0	1	121	97	217	2.54e-36	141	Eukaryota	Trichuris trichiura	36087

    $ head out.1e-5.max500.taxids.txt
    nHd.2.3.1.t00019-RA	OQV20892.1	100.000	122	0	0	1	122	1	122	4.77e-85	253	Eukaryota	Hypsibius dujardini	232323
    nHd.2.3.1.t00019-RA	GAV08169.1	75.806	124	30	0	1	124	51	174	5.53e-45	162	Eukaryota	Ramazzottius varieornatus	947166
    nHd.2.3.1.t00019-RA	WP_042303394.1	58.678	121	49	1	4	124	93	212	1.01e-40	153	Bacteria	Burkholderia kururiensis	984307
    nHd.2.3.1.t00019-RA	WP_017775351.1	58.678	121	49	1	4	124	93	212	1.13e-40	153	Bacteria	Burkholderia kururiensis	984307
    nHd.2.3.1.t00019-RA	KRX89027.1	63.115	122	45	0	1	122	105	226	7.01e-37	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KRX89025.1	63.115	122	45	0	1	122	105	226	1.43e-36	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KFD69381.1	61.983	121	46	0	1	121	466	586	1.85e-36	141	Eukaryota	Trichuris suis	68888
    nHd.2.3.1.t00019-RA	KRZ17714.1	63.115	122	45	0	1	122	121	242	1.86e-36	140	Eukaryota	Trichinella pseudospiralis	6337
    nHd.2.3.1.t00019-RA	KFD48812.1	61.983	121	46	0	1	121	419	539	1.92e-36	141	Eukaryota	Trichuris suis	68888
    nHd.2.3.1.t00019-RA	KHJ41189.1	61.983	121	46	0	1	121	39	159	1.98e-36	141	Eukaryota	Trichuris suis	68888

    $ cat out.1e-5.max100.taxids.txt out.1e-5.max500.taxids.txt | grep -v "Hypsibius dujardini" | grep -v "Ramazzottius varieornatus" | cut -f 2 | sort | uniq > older_matches.txt
    $ blastdbcmd -entry_batch older_matches.txt -db nr -dbtype prot > older_matches.fasta
    $ grep -c "^>" older_matches.fasta 
    496
    $ wc -l older_matches.txt 
    496 older_matches.txt


# Creating taxid map older_matches.taxmap.txt

Derive full taxid map from the blast output using the 2018 NR database:

    $ cat out.1e-5.max100.taxids.txt out.1e-5.max500.taxids.txt | grep -v "Hypsibius dujardini" | grep -v "Ramazzottius varieornatus" | cut -f 2,15 | cut -f 1 -d ";" | sort | uniq > older_matches.taxmap.txt

Note the messing about with the semi-colon as makeblastdb does not tolerate
multiple taxid values for an entry.


# Build the test database


Build older_matches.fasta BLAST database
    
    $ makeblastdb -dbtype prot -in older_matches.fasta -parse_seqids -taxid_map older_matches.taxmap.txt
    Building a new DB, current time: 10/10/2018 11:56:09
    New DB name:   /mnt/shared/users/pc40583/repositories/max_target_seqs/tests/older_matches.fasta
    New DB title:  older_matches.fasta
    Sequence type: Protein
     Deleted existing Protein BLAST database named /mnt/shared/users/pc40583/repositories/max_target_seqs/tests/older_matches.fasta
    Keep MBits: T
    Maximum file size: 1000000000B
    Adding sequences from FASTA; added 496 sequences in 0.0551929 seconds.


# Reproduce the issue

This works for reproducing the original problem, in that the top bacterial match comes and goes with changes to -max_target_seqs
    
    $ blastp -query input.fasta -db older_matches.fasta -outfmt "6 std sskingdoms" -max_target_seqs 100 -evalue 1e-5 | head
    nHd.2.3.1.t00019-RA KRX89027.1      63.115  122     45      0       1       122     105     226     5.26e-42        140     Eukaryota
    nHd.2.3.1.t00019-RA KRX89025.1      63.115  122     45      0       1       122     105     226     1.07e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA KFD69381.1      61.983  121     46      0       1       121     466     586     1.39e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KRZ17714.1      63.115  122     45      0       1       122     121     242     1.39e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA KFD48812.1      61.983  121     46      0       1       121     419     539     1.44e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KHJ41189.1      61.983  121     46      0       1       121     39      159     1.49e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KRX89026.1      63.115  122     45      0       1       122     153     274     1.82e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA CDW52156.1      61.983  121     46      0       1       121     97      217     1.90e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KRZ35475.1      63.115  122     45      0       1       122     105     226     2.77e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA KRX89032.1      63.115  122     45      0       1       122     105     226     2.95e-41        140     Eukaryota
    
    $ blastp -query input.fasta -db older_matches.fasta -outfmt "6 std sskingdoms" -max_target_seqs 500 -evalue 1e-5 | head
    nHd.2.3.1.t00019-RA WP_042303394.1  58.678  121     49      1       4       124     93      212     7.54e-46        153     Bacteria
    nHd.2.3.1.t00019-RA WP_017775351.1  58.678  121     49      1       4       124     93      212     8.49e-46        153     Bacteria
    nHd.2.3.1.t00019-RA KRX89027.1      63.115  122     45      0       1       122     105     226     5.26e-42        140     Eukaryota
    nHd.2.3.1.t00019-RA KRX89025.1      63.115  122     45      0       1       122     105     226     1.07e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA KFD69381.1      61.983  121     46      0       1       121     466     586     1.39e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KRZ17714.1      63.115  122     45      0       1       122     121     242     1.39e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA KFD48812.1      61.983  121     46      0       1       121     419     539     1.44e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KHJ41189.1      61.983  121     46      0       1       121     39      159     1.49e-41        141     Eukaryota
    nHd.2.3.1.t00019-RA KRX89026.1      63.115  122     45      0       1       122     153     274     1.82e-41        140     Eukaryota
    nHd.2.3.1.t00019-RA CDW52156.1      61.983  121     46      0       1       121     97      217     1.90e-41        141     Eukaryota
