#!/bin/bash

curl "http://localhost:8000/answers/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "answer": {
      "answer_title": "'"${ANSWER_TITLE}"'",
      "answer": "'"${ANSWER}"'"
    }
  }'

echo
