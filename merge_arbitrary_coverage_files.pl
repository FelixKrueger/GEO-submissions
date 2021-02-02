#!/usr/bin/perl
use warnings;
use strict;
my @files = <*cov.gz>;
my %groups;


my %cov;

foreach my $file (@files) {
    print "Now reading file $file\n";
	
	open (IN,"zcat $file |") or die $!;
	while (<IN>){
	    chomp;
	    my ($chr,$pos,$m,$u) = (split "\t")[0,1,4,5];
	    $cov{$chr}->{$pos}->{m} += $m;
	    $cov{$chr}->{$pos}->{u} += $u;
	    # print  $cov{$chr}->{$pos}->{m},"\n";
	    # print  $cov{$chr}->{$pos}->{u},"\n"; sleep(1);
	    
	    # print join ("\t",$chr,$pos,$m,$u),"\n"; sleep(1); 
	}
	close IN;
}

my $outfile = "_merged.cov.gz";
warn "Outfile will ne named:\n$outfile\n\n"; sleep(1);

open (OUT,"| gzip -c > $outfile") or die $!;
 
warn "Now printing a new, merged coverage file\n";
foreach my $chr(sort keys %cov){
    foreach my $pos(sort {$a<=>$b} keys %{$cov{$chr}}){
	my $perc = sprintf ("%.2f", $cov{$chr}->{$pos}->{m} / ($cov{$chr}->{$pos}->{m} + $cov{$chr}->{$pos}->{u}) *100 );
	print OUT "$chr\t$pos\t$pos\t$perc\t$cov{$chr}->{$pos}->{m}\t$cov{$chr}->{$pos}->{u}\n";
    }
}
close OUT or die $!;

print "\n"; sleep(1);


