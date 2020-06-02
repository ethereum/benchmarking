#!/bin/bash

HERE=`pwd`
cd ../rawdata
FILES=geth*
for f in $FILES
do 
  echo "Processing $f"
  python ../scripts/postprocess_geth_v2.py $f > ../processed/$f.md
done
FILES=cpp*
for f in $FILES
do 
  echo "Processing $f"
  python ../scripts/postprocess_cpp.py $f > ../processed/$f.md
done
FILES=parity*
for f in $FILES
do 
  echo "Processing $f"
  python ../scripts/postprocess_parity.py $f > ../processed/$f.md
done

cd $HERE

