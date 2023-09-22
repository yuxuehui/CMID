#!/bin/bash

#SBATCH --job-name=hopper      #作业名称
#SBATCH --ntasks=1
#SBATCH --time=100:00:00     #申请运行时间
#SBATCH --output=%j.out                #作业标准输出
#SBATCH --error=%j.err                   #作业标准报错信息
#SBATCH -p agents2
#SBATCH --gres=gpu:1                   #申请1张GPU卡

source ~/.bashrc     #激活conda环境
conda activate dmcontrol

python train_SAC.py --domain_name hopper --task_name stand --algorithm drq --device gpu --seed 0 --num_train_steps 50000

