#!/bin/bash

curl "http://localhost:8000/questions" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "topic": "'"${TOPIC}"'",
      "content": "'"${CONTENT}"'"
    }
  }'

echo
