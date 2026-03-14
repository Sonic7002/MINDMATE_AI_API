#!/bin/bash

TEXT="$1"
VOICE="$2"
OUTPUT="$3"
API_KEY="$NVIDIA_API_KEY"


python3 python-clients/scripts/tts/talk.py \
    --server grpc.nvcf.nvidia.com:443 --use-ssl \
    --metadata function-id "877104f7-e885-42b9-8de8-f6e4c6303969"  \
    --metadata authorization "Bearer $API_KEY" \
    --language-code en-US \
    --text "$TEXT" \
    --voice "Magpie-Multilingual.EN-US.$VOICE" \
    --output $OUTPUT
