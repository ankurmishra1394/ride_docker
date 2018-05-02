#!/usr/bin/env bash

while true
do
	python /receive.py
	tc_name="$(head -1 /tmp/test_case_name.txt)"
	tc_link="$(head -1 /tmp/test_case_link.txt)"
	tc_path="$(head -1 /tmp/test_case_path.txt)"
	/usr/bin/wget "$tc_link"
	python /usr/local/bin/ride.py "$tc_name"
done