#!/bin/bash -eu
DATE=`date +"%Y%m%d %H:%M%S"`
ROOM=22313530
BODY="example test (postdatetime=${DATE})"

LOC="http://localhost:8088"
POSTPATH="chatwork/message"
POSTURL="${LOC}/${POSTPATH}/${ROOM}"

echo $POSTURL
curl -s -d "body=${BODY}" "${POSTURL}"
echo 'end'
