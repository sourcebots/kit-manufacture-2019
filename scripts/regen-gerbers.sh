#!/bin/sh
set -o errexit -o nounset -o pipefail

scripts_dir=$(dirname $0)
repo_dir=$scripts_dir/..

for board_name in $*; do
  pcb_file=$repo_dir/$board_name-v4-hw/$board_name.pcb
  gerber_dir=$repo_dir/quote-pack/$board_name/gerbers

  rm -rf $gerber_dir
  mkdir -p $gerber_dir
  pcb -x gerber --gerberfile $gerber_dir/$board_name $pcb_file
done
