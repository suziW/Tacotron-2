#!/bin/sh
for i in BZNSYP/Wave/*.wav;
do
ffmpeg -i "$i" -ar 16000 "BZNSYP/downsampled/${i##*/}";
done
