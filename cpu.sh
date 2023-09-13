#!/bin/bash

#SBATCH --job-name=sac      #作业名称
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=60:00:00     #申请运行时间
#SBATCH --mem-per-cpu=4G
#SBATCH --output=./output/%j.out                #作业标准输出
#SBATCH --error=./output/%j.err                   #作业标准报错信息


source ~/.bashrc     #激活conda环境
conda activate dmcontrol

python train_copy.py 

