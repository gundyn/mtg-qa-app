#!/bin/bash

curl "http://localhost:8000/answers/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
