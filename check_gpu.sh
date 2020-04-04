#!/bin/bash
#!/bin/sh  
while true  
do  
  nvidia-smi > gpu
  python3 check_gpu.py
  sleep 300  
done
