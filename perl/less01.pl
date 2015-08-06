#!/usr/bin/perl
#
print "hello perl\n";
print "hello,","world\n";
print ("it's such a perfect day!\n");
printf("Meet %s:Age %5d:Salary \$%10.2f\n","Leicx",27,5500000);

$first_name="chongxiang";
$last_name="Lee";
$sala= 21000.00;
print qq#$first_name, $last_name, $sala\n#;

print qq#**********************************\n#;
@nums=(1,7,4,6,8,9);
print "@nums\n";
print "$nums[3]\n";
@num_2 = sort(@nums);
print "@num_2\n";
