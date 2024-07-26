#!/bin/bash

flag_start = $1
flag_end = $2
file_name = $3

grep -oP '(?<=$flag_start).*(?=$flag_end)' file_name
