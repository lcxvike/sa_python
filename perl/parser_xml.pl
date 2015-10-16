#!/usr/bin/perl
#
use XML::Simple;
use Data::Dumper;

$xml = XMLin('xmlfile.xml');
print Dumper($xml);
