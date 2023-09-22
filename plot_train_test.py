# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号
import os

out_file_name = ["/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8/sac/0/eval.csv", 
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8/sac/0/train.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed1/sac/1/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed1/sac/1/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed2/sac/2/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed2/sac/2/train.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed3/sac/3/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed3/sac/3/train.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed4/sac/4/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed4/sac/4/train.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed10/sac/10/eval.csv",
                    "/scratch/yxue/CMID/runs/cartpole_damping_10000_ar8_seed10/sac/10/train.csv"
                ]

for file_index in range(len(out_file_name)):
    x_ep_train = []
    x_ep_adapt = []
    x_dim = []
    f = open(out_file_name[file_index])               # 返回一个文件对象 
    line = f.readline()               # 调用文件的 readline()方法 
    while line: 
        if "step" not in line:
            x_ep_train.append(float(line.split(',')[-2].strip()))
            x_dim.append(int(line.split(',')[-1].strip()))
        line = f.readline()
    for i in range(int(len(x_dim)/2), int(len(x_dim))):
        x_dim[i] = x_dim[i] + x_dim[int(len(x_dim)/2)-1]
        # print(x_dim[int(len(x_dim)/2)-1])
        # print(x_dim[i])
        # raise

    
    y = np.array(x_ep_train)
    x = np.array(x_dim)


    plt.figure(figsize=(10,5))
    plt.grid(linestyle = "--") 
    ax = plt.gca()
    ax.spines['top'].set_visible(False) #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框

    plt.plot(x,y,color="black",label=out_file_name[file_index],linewidth=1.5)
    plt.vlines(x[int(len(x_dim)/2)], np.min(y), np.max(y), colors = "r", linestyles = "dashed")

    plt.ylabel("ep_rew_mean",fontsize=13,fontweight='bold')
    plt.xlabel("Time steps",fontsize=13,fontweight='bold')
    # plt.xlim(3,21) #设置x轴的范围
    # plt.ylim(0.5,1)

    #plt.legend()          #显示各曲线的图例
    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=12,fontweight='bold') #设置图例字体的大小和粗细

    plt.savefig(out_file_name[file_index] + ".png") #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中

    f.close()  

