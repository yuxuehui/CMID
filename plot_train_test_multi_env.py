# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号
import os

def load_file(out_file_name):
    x = np.array([])
    y = []

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
        if len(x)==0:
            x = np.array([x_ep_train.copy()])
        else:
            x = np.insert(x, 0, values=x_ep_train.copy(), axis=0)
        f.close()  
    # mean
    y = np.array(x_dim.copy())
    x_mean = np.mean(x, axis=0)
    x_max = np.max(x, axis=0)
    x_min = np.min(x, axis=0)
    return y, x_mean, x_max, x_min

def plot_function(y, x_mean, x_max, x_min, label_name = "default", save_dir = "default"):
    f = plt.figure(figsize=(10,5))
    plt.grid(linestyle = "--") 
    ax = plt.gca()
    ax.spines['top'].set_visible(False) #去掉上边框
    ax.spines['right'].set_visible(False) #去掉右边框

    plt.plot(y,x_mean,color="black",linewidth=1.5)
    plt.vlines(y[int(len(y)/2)], np.min(x_mean), np.max(x_mean), colors = "r", linestyles = "dashed")
    plt.fill_between(y, x_max, x_min, #上限，下限
            facecolor='grey', #填充颜色
            # edgecolor='red', #边界颜色
            alpha=0.3) #透明度

    plt.ylabel("ep_rew_mean",fontsize=13,fontweight='bold')
    plt.xlabel("Time steps",fontsize=13,fontweight='bold')
    # plt.xlim(3,21) #设置x轴的范围
    # plt.ylim(0.5,1)
    plt.title(label_name)
     
    # plt.legend(loc=0, numpoints=1)
    # leg = plt.gca().get_legend()
    # ltext = leg.get_texts()
    # plt.setp(ltext, fontsize=12,fontweight='bold') #设置图例字体的大小和粗细

    plt.savefig("/scratch/yxue/CMID/runs/" + save_dir + ".png") #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中

if __name__ == "__main__":
    out_file_name_train = [
                    "/scratch/yxue/CMID/runs/cartpole_damping_slide_envA_5e-10_envB_10_30000_seed0/sac/0/train.csv"
    ]

    out_file_name = ["runs/cartpole_damping_slide_envA_5e-10_envB_10_30000_seed0/sac/0/eval.csv"
                ]
    y, x_mean, x_max, x_min = load_file(out_file_name = out_file_name)
    plot_function(y, x_mean, x_max, x_min, label_name = "Cartpole damping_slide; Evaluation; Multi-envs-5; ar_8; envA 5e-10; envB 10; Train_steps_30000", save_dir ="cartpole_damping_slide_eenvA_5e-10_envB_10")

    y, x_mean, x_max, x_min = load_file(out_file_name = out_file_name_train)
    plot_function(y, x_mean, x_max, x_min, label_name = "Cartpole damping_slide; Training; Multi-envs-5; ar_8; envA 5e-10; envB 10; Train_steps_30000", save_dir ="cartpole_damping_slide_train_envA_5e-10_envB_10")