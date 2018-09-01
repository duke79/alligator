#!/usr/bin/env bash
curl -X POST  http://192.168.1.101/graph -H "ontent-type: multipart/form-data;" -F "query={ currentUser { feed(action: {get: {userId: 1, sortBy: [CATEGORY], sortOrder: [false], limit: 1000}}) { title category } }}"
