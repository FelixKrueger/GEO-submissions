#!/usr/bin/env python

import os
import glob
import time
import gzip

print ("Merging Arbitrary Bismark coverage files")
cov_files = glob.glob("*.cov.gz")

allcov = {} # overarching dictionary

for file in cov_files:
    print (f"Reading methylation calls from file: {file}")

    isGzip = False
    if file.endswith("gz"):
        infile = gzip.open(file) # mode is 'rb' 
        isGzip = True
    else:
        infile = open(file)

    for line in infile:
        
        if isGzip:
            line = line.decode().rstrip() # need to decode from a Binary to Str object
        else:
            line = line.rstrip()

        # print(line)
        # chrom, pos, m, u = line.split(sep="\t")[0,1,4,5]
    
        chrom, pos, m, u = [line.split(sep="\t")[i] for i in (0,1,4,5)] # list comprehension

        if chrom in allcov.keys():
            pass
            # print (f"already present: {chrom}")
        else:
            allcov[chrom] = {}
            
            # print (f"Key not present yet for chromosome: {chrom}. Creating now")
        # converting the position to int() right here
        pos = int(pos)

        if pos in allcov[chrom].keys():
            # print (f"Positions was already present: chr: {chrom}, pos: {pos}")
            pass
        else:
            allcov[chrom][pos] = {}
            allcov[chrom][pos]["meth"] = 0
            allcov[chrom][pos]["unmeth"] = 0

        allcov[chrom][pos]["meth"] += int(m) 
        allcov[chrom][pos]["unmeth"] += int(u)
        
        # print (f"Chrom: {chrom}")
        # print (f"Chrom: {chrom}, Pos: {pos}, Meth: {m}, Unmeth: {u}")
        # time.sleep(0.1)

    infile.close()




print ("Now printing out a new, merged coverage file")

# resetting
del chrom
del pos

with gzip.open("merged_coverage_files.cov.gz","wt") as out:
    # Just sorting by key will sort lexicographically, which is unintended.
    # At least not for the positions
    for chrom in sorted(allcov.keys()):
        
        # Option I: This is a solution using {} dictionary comprehension. Seems to work.
        # print (f"Converting position keys to int first for chromosome {chrom}")
        # allcov[chrom] = {int(k) : v for k, v in allcov[chrom].items()}

        # Option II: Another option could be to use a Lambda function to make the keys integers on the fly
        # print (f"Attempting solution using a Lambda function on the positions for chrom:{chrom}")
        # for pos in sorted(allcov[chrom].keys(), key = lambda x: int(x)):
        # This also works

        # Option III: Since I changed the values going into the positions dictionary, sorted()
        # will now automatically perform a numerical sort. So no further action is required.
        print (f"Now sorting positions on chromosome: {chrom}")
        for pos in sorted(allcov[chrom].keys()):
            perc = ''
            if (allcov[chrom][pos]['meth'] + allcov[chrom][pos]['unmeth'] == 0):
                # This should not happen in real data, as coverage files by definition only show covered positions
                print ("Both methylated and unmethylated positions were 0. Dying now...")
                sys.exit()
            else:
                perc = allcov[chrom][pos]['meth'] / (allcov[chrom][pos]['meth'] + allcov[chrom][pos]['unmeth']) * 100
            
            # percentage is displayed with 2 decimals with f-string formatting
            out.write(f"{chrom}\t{pos}\t{pos}\t{perc:.2f}\t{allcov[chrom][pos]['meth']}\t{allcov[chrom][pos]['unmeth']}\n")

print ("All done, enjoy the merged coverage file!\n")