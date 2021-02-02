# Submitting sequencing data to GEO - some thoughts

Here are a few considerations about GEO submissions; some are more general, others are specifically tailored towards submissions from the Babraham Institute.

The entire submission process is described in detail over at the [GEO high-throughput sequencing data submission](https://www.ncbi.nlm.nih.gov/geo/info/seq.html) pages, here we focus on the more practical implications. While GEO handles the metadata and quantitation of your submission, the raw sequencing data itself is handled by the [Sequencing Read Archive](https://www.ncbi.nlm.nih.gov/sra), and will be available via the [NCBI](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?), the European [ENA](https://www.ebi.ac.uk/ena/browser/home) or the Japanese [DDBJ](https://www.ddbj.nig.ac.jp/dra/index-e.html). For a quick look and easy way to retrieve raw data from the SRA take a look at the [SRA-Explorer](https://sra-explorer.info/).

**The submission process**

To submit sequencing data to the GEO repository you will need:
 - raw sequencing data (`FastQ` files), as well as 
 - some kind of application-sepcific quantitation (a `BAM` file is not sufficient), as well as
 - a metadata spreadsheet detailing the experiment and how the files are related to each other
 

## Submission from Babraham

- contact Babraham Bioinformatics with a list of files, the sample name as well as the desired name of the sample for the manuscript, e.g.:

```
SierraID      sample name on Sierra                name in manuscript
  4777     lane4777_TAGCATAG_GAGAGTCT_....           Dnmt1_WT_rep1
...
```

- we will take a look, collate all necessary files and return to you a the metadata spreadsheet (see below) to fill in the details

- please **do not** start by filling in the metadata spreadsheet with filenames and details, as this will make it much harder for us to produce the spreadsheet, and is also considerably more prone to errors.


## Quantified files

The quantitation can more or less be anything that you deem useful for your data. In all cases, the file format and its contents need to be described in a way that leaves no doubts (e.g. the RNA-seq report is a tab-delimited text file (SeqMonk Annotated Probe report) showing log2 RPM values for each gene (Ensembl GeneID)).

peak quantitation for ChIP and percent methylation over whatever windows you used for methylation data.

### Bisulfite-seq 

This is fairly straight forward, both Bismark coverage files (ending in `.cov.gz`) or genome-wide cytosine reports are acceptable. Coverage files are preferred as they are generated by default, less unwieldy and more precise (see here for differences between the two different file formats: [difference between coverage and cytosine report files](https://github.com/FelixKrueger/Bismark/blob/master/Docs/FAQ.md#context-changediscrepancy-between-bismark-coverage-and-genome-wide-cytosine-reports)

### RNA-seq

Typically some sort of measure of gene expression. This can be a gene matrix in R, a SeqMonk probe report, fold-change tables etc. A single matrix for all samples would be fine.

### ChIP-seq/ATAC-seq etc

Acceptable here would be peak calling files and/or annotation, but also a tiled-window quantitation genome-wide is a good choice. A single matrix for all samples would be fine.

## The metadata spreadsheet

A template for the metadata spreadsheet can be downloaded from GEO here: https://www.ncbi.nlm.nih.gov/geo/info/examples/seq_template.xlsx
This is really just for your information, we will 




### Reviewer token



