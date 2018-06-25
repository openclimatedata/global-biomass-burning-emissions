#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $DIR/../raw_data
cat ../files.txt | awk '{print $1}' | xargs wget --no-clobber
