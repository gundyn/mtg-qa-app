#!/bin/bash

curl "http://localhost:8000/answers/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
