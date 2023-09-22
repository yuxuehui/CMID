#!/bin/bash

#SBATCH --job-name=chee_damp      #作业名称
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=150:00:00     #申请运行时间
#SBATCH --mem-per-cpu=4G
#SBATCH --output=./output/%j.out                #作业标准输出
#SBATCH --error=./output/%j.err                   #作业标准报错信息


source ~/.bashrc     #激活conda环境
conda activate dmcontrol

# python train_SAC.py --domain_name hopper --task_name stand --algorithm sac --seed 10 --num_train_steps 1000000
python train_SAC.py --domain_name cartpole --task_name swingup --description cart_friction_ --algorithm sac --seed 0 --num_train_steps 100000
# python train_SAC.py --domain_name cartpole --task_name swingup --description cart_friction_ --algorithm sac --seed 5 --num_train_steps 30000
# python train_SAC.py --domain_name cartpole --task_name swingup --description cart_friction_ --algorithm sac --seed 10 --num_train_steps 30000
# cart_friction_ / mass_capsule_ / mass_cart_


# used for walker-walk, add the module of saving models
# python train_other.py --domain_name cheetah --task_name run --description damping_ --algorithm sac --seed 0 --num_train_steps 1000000
# python train_other.py --domain_name walker --task_name walk --description damping_ --algorithm sac --seed 0 --num_train_steps 400000
# python train_other.py --domain_name walker --task_name walk --description mass_ --algorithm sac --seed 0 --num_train_steps 400000
# mass_ / damping_

# python train_other.py --domain_name hopper --task_name stand --algorithm sac --seed 0 --num_train_steps 1000000