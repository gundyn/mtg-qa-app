#!/bin/bash

curl "http://localhost:8000/answers" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
