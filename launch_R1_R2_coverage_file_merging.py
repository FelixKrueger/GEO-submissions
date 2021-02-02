#!/usr/bin/env python

import os
import glob
from time import sleep as sleep
import gzip
import subprocess
import re
import argparse

def main():
    
    print ("Parsing options")
    options = parse_options()
    sleep(1)
    print("     :::::\n\nMerging Arbitrary R1 and R2 coverage files")
 
    cov_files = glob.glob("G*NOM*.cov.gz")
    # print (cov_files)
    cov_files.sort()
    print (cov_files)

    print("     :::::\n\n")
    sleep(1)
    # To process a set of files, we need to take 2 files
    while len(cov_files) >= 2:
        file1 = cov_files.pop(0)
        file2 = cov_files.pop(0)

        process_set_of_files(file1,file2,options)


def parse_options():
    parser = argparse.ArgumentParser(description="Run a command on the cluster")

    parser.add_argument("--dryrun", help="Don't run anything, just say what you would do", action="store_true")
    options=parser.parse_args()

    return options

def process_set_of_files(file1,file2,options):
    # print (f"processing the following set of files: {file1} and {file2}")
    # GSM4056543_32cell_embryoMixed_25_NOMe-seq_R1_GRCm38_bismark_bt2.deduplicated.bismark.cov.gz
    pattern = re.compile("(.*)_NOMe-seq")
    
    m = pattern.match(file1)
    if m:
        pass
        # print('Match found: ', m.group(1))
    else:
        pass
        print('No match')

    # check if it is also present for file2
    #print (file2)
    # print (m.group(1))
    basename = m.group(1)
    if file2.startswith(f"{m.group(1)}"):
        # print (f"Yes, it does!")
        pass
    else:
        print ("Nah...")
        sys.exit()

    print ("Ready to launch merging process for:")
    print (basename)
    print (file1)
    print (file2)
    print ("     ::::::     \n")

    command = f"/bi/home/fkrueger/VersionControl/stonecluster/bin/ssub.py -o {basename}.log --email --mem 150G /bi/scratch/scripts/headstone/merge_coverage_files_ARGV.py"
    # print (f"Command:\n{command}")
    arguments = f"--basename {basename} {file1} {file2}"
    # print (f"Arguments:\n{arguments}")

    full_command = f"{command} {arguments}"
    if options.dryrun:
        print("Dry-Run Command\n===============")
        print(f"{full_command}\n\n")
        # bismark --pbat --genome /bi/scratch/Genomes/Human/GRCh38_dbSNP_N-masked/dbSNP_N-masked/ -1 test_R1.fq.gz -2 test_R2.fq.gz
    else:
        # This works, but shell=True may be a security issue. Instead, use ['list','of','arguments']
        # for using a user given input, see the fix_spaces function below. The way of using a String with shell=True
        # does not require this fixing right now
       subprocess.run(f"{full_command}",shell=True, check = True)

        # Also works with an os.system() command, but this is now deprecated
        # os.system(full_command)


    def fix_spaces():

        # If the user put an option with spaces in it in their command
        # then this will be included as a single argument to ARGV, but
        # we won't be able to spot it later.  We need to add in quotes
        # if we find this.

        for i in range(len(sys.argv)):
            if (" " in sys.argv[i]):
                sys.argv[i] = '"'+sys.argv[i]+'"'

# print ("All done, enjoy the merged coverage file!\n")

if __name__ == "__main__":
    main()