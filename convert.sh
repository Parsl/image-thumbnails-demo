export PATH=$PATH:~wozniak/Public/sfw/compute/swift-t/stc/bin
export CRAY_PPN=true
export WALLTIME=00:10:00
export PROCS=304
export PPN=16
export TURBINE_OUTPUT=$HOME/photos/turbine.d

ls -1 IM* > foto_list.txt
cp foto_list.txt $TURBINE_OUTPUT
cp IM* $TURBINE_OUTPUT
mkdir $TURBINE_OUTPUT/.resampled
module load bwpy
TURBINE_LOG=1 \
ADLB_PRINT_TIME=1 \
  swift-t -m cray -n 304 convert.swift
  #swift-t -n 8 convert.swift
