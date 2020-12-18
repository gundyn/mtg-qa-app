#!/bin/bash

curl "http://localhost:8000/questions/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "question": {
      "topic": "'"${TOPIC}"'",
      "content": "'"${CONTENT}"'"
    }
  }'

echo
