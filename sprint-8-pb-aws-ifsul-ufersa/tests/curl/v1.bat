@echo off
curl -X POST https://uc06urph01.execute-api.us-east-1.amazonaws.com/v1/vision -H "Content-Type: application/json"    -d "@v1.json"
