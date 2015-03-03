#!/bin/bash
awk '{ for(i=2;i<=NF;i++) num[$i]++ } END{ for(x in num) printf("%10s = %d\n",x,num[x]) }' awk_arr.conf
