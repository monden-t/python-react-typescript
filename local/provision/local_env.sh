#!/bin/bash

# hostの環境変数定義用shell
echo 'set up ENV'

echo "export REDIS_HOST=localhost" >> ~/.profile
echo "export REDIS_PORT=6379" >> ~/.profile
echo "export REDIS_DB_NO=0" >> ~/.profile
