#!/usr/bin/perl
#
use XML::DOM;
use Data::Dumper;

$book_xml="books.xml";
sub init_xml
{
###读取xml文件
	my $xmlfile="$book_xml";
	my $parser= new XML::DOM::Parser;
	
	my $doc = $parser->parsefile($xmlfile)||die "parse $xmlfile error\n";
	my $n_bookstore = $doc->getElementsByTagName("bookstore");
	
	my $n_book = $n_bookstore->item(0)->getElementsByTagName("book");
	my $n_year = $n_bookstore->item(0)->getElementsByTagName("year");
	my $year = $n_year->item(0)->getAttributeNode("year")->getValue;
	
	print "$year\n";
}

&init_xml;
