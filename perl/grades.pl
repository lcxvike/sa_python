#!/usr/bin/perl -w

open(GRADES,"students.txt") or die "Can't open grades: $!\n";
while($line = <GRADES>)
{
	($student,$grade) = split("	", $line);
	$grades{$student} = $grade . " ";
	
}

$scores = 0;
$total = 0;
foreach $student (sort keys %grades)
{
	@grades = split(" ",$grades{$student});
	foreach $grade (@grades)
	{
		$total += $grade;
		$scores++; 
	}
	print "$student : $grades{$student}";
}

$aver = $total/$scores;
print "Aver:$aver\n"
