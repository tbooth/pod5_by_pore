# Re-sort POD5 files by channel

## Motivation

Oxford Nanopore Technologies MinKNOW software saves the signal output from MinION and PromethION
flowcells in the POD5 format. Recently, the number of POD5 files has been reduced as more reads
are batched into each single file, but the organisation of the reads in the files has not been
changed. They are approximately, but not strictly, grouped by the time of recording.

This is significant for duplex basecalling, where the two reads in a duplex pair may or may not
be in the same POD5 file. Partitioning the files by pore (ie. by channel) guarantees that duplex
pairs will be together in a file, and so individual POD5 files, or batches thereof, may be
meaningfully processed with "dorado duplex".

For archiving of POD5 files, formatting by partition may therefor be useful. This workflow does the
re-partitioning efficiently with a configurable batch size.

## Configuration

The workflow accepts two `--config` parameters:

    * **input** (mandatory) - the directory containing input POD5 files. This may be an absolute
      path or a direcotory within the working directory. The workflow will scan this directory
      recursively for all `.pod5` files.
    * **ppp** (default 50) - the number of pores (channels) to include in each output file. If
      this is set to anything other than 1 the range of pores will be recorded in the output file
      names as `x-y` where `x` and `y` are channel numbers and are inclusive. NanoPore numbers
      channels from 1.

## Output

The `results` directory will contain the partitioned POD5 files. There will also be working files
under results/tmp which may be discarded once the workflow is complete.

## Dependencies

The workflow needs the **pod5** tool which may be installed using the supplied Conda environment
definition. Note that there is no conda package for this at present so it will actually be
installed via pip. Modern Conda installations should handle this automatically.

## Cluster execution

This workflow will benefit from running on a cluster with a shared filesystem. Note that, since
the `pod5_for_channel` rule is likely to need all of the POD5 files as input to every job, an
execution environment that stages the inputs and outputs from a remote storage provider will not
run the workflow very efficiently.

## Compatibility

This has been tested on MinION and PromethION outputs, and should work regardless of whether the
input POD5 files are in the old organisation (with 4000 reads per file) or the newer layout with
fewer, larger files.


