# Workflow tests

## Testing the workflow

You can run a basic test of the workflow using the files in this directory. You will need to have
Snakemake and conda installed.

```
$ snakemake --use-conda -j1 --config input=tests/integration ppp=100
```

## integration

This directory contains some toy data files to test the whole workflow. These are useful for:

* CI testing (which is enabled on GitHub)
* Checking the workflow runs on your local environment
* Auto-generating the unit tests
* Generating workflow/dag.dot (and from this workflow/dag.png)

DAG generation command is:

```
$ snakemake --configfile tests/integration.yaml --dag
```

## unit

This directory contains the auto-generated unit tests created by Snakemake:

```
$ snakemake --use-conda -j1 --configfile tests/integration.yaml --generate-unit-tests
```
