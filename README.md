# Overview

20440_proj contains data and code files that (will) compare inflammation and cancer data using 
PCA and clustering techniques to understand trends in protein expression levels among disease. 
Functionally, there is currently a script to load in gastric disease data and plot protein 
expression of 20 proteins in one replicate of each condition. 

## Data
Data was generated from experimental data of three papers and found publicly online or 
through contacting the first-author.
Datasets are from: 
- Haudek-Prinz VJ, …, Gerner C. Proteome signatures of inflammatory activated primary 
human peripheral blood mononuclear cells. J Proteomics. 2012 Dec 5;76 Spec No.(5):150-62. 
doi: 10.1016/j.jprot.2012.07.012.
- Fernández-Coto DL, …, Ayala G. Quantitative proteomics reveals proteins involved in the 
progression from non-cancerous lesions to gastric cancer. J Proteomics. 2018 Aug 30;186:15-27. 
doi: 10.1016/j.jprot.2018.07.013. 
- McCaffrey EF, …, Angelo M. Multiplexed imaging of human tuberculosis granulomas uncovers 
immunoregulatory features conserved across tissue and blood. bioRxiv 2020.06.08.140426; 
doi: 10.1101/2020.06.08.140426.

## Structure
- code_EDA/
	- Python and Jupyter Notebook file for loading and plotting preliminary figure of
	gastric data 
- data/
	- raw/
		- raw dataset, entire spreadsheet files
	- processed/ 
		- (will) contain cleaned/relevant lines of data from original datasets
- figures
	- results from plotting (currently, one preliminary figure of protein expression of 
	one set of gastric data) 

## Installation/Usage 
Packages used include pandas (1.1.2), numpy (1.19.2), and matplotlib (3.3.2). You can run 
Python (v3.8.3) files in an IDE and generate associated figures, after making sure the data 
files are in the same folder as your script. Jupyter Notebook or Conda may be needed to run 
.ipynb files.
