#!/bin/bash

INPUT="$1"
API_KEY="$NVIDIA_API_KEY"


python3 python-clients/scripts/asr/transcribe_file_offline.py \
    --server grpc.nvcf.nvidia.com:443 --use-ssl \
    --metadata function-id "b702f636-f60c-4a3d-a6f4-f3568c13bd7d" \
    --metadata "authorization" "Bearer $API_KEY" \
    --language-code en \
    --input-file $INPUT