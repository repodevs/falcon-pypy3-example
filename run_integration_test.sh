#!/bin/bash

# Run Test with httpie and jq

# Trigger Create Task
test_1=`http POST http://127.0.0.1:9099/task/create number=3 | jq -r '.data.task_id'`

# Get Task Status
check_test=`http GET http://127.0.0.1:9099/task/status/${test_1} | jq -r '.status'`

# Loop Until Get Status `SUCCESS`
while [ "$check_test" != "SUCCESS" ]
do
    check_test=`http GET http://127.0.0.1:9099/task/status/${test_1} | jq -r '.status'`
    echo $(http GET http://127.0.0.1:9099/task/status/${test_1})
done
