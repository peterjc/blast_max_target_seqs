Creating a test database to reproduce the original bug report from
https://gist.github.com/sujaikumar/504b3b7024eaf3a04ef5
http://blastedbio.blogspot.co.uk/2015/12/blast-max-target-sequences-bug.html

Idea is to capture all the current NR matches to the query, and then
excluding the recent tardigate sequences which were not present back
in December 2015.

(1) Creating older_matches.fasta

Using NR data 2018-06-08 (8 June 2018)

$ export BLASTDB=/mnt/shared/cluster/blast/ncbi/extracted/
$ time blastp -query input.fasta -db nr -outfmt "6 std sskingdoms sscinames staxids" -max_target_seqs 500 -evalue 1e-5 >out.1e-5.max500.taxids.txt

real	14m10.383s
user	10m9.971s
sys	0m31.278s

$ time blastp -query input.fasta -db nr -outfmt "6 std sskingdoms sscinames staxids" -max_target_seqs 100 -evalue 1e-5 >out.1e-5.max100.taxids.txt

real	12m5.952s
user	9m26.712s
sys	0m20.455s

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
