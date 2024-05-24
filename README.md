# pod5_by_pore

A Snakemake workflow to take the POD5 files produced by an Oxford Nanopore sequencing run and
re-batch them by pore (ie. by channel).

This is useful if you want to run duplex basecalling because you can meaningfully run
"dorado duplex" on a single (or a subset of) the POD5 files.

## Know issues

It is assumed all POD5 input files are from the same sequencing run, but this is not checked.
