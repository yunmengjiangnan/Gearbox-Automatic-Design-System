# Gearbox-Automatic-Design-System1212

## 简介

减速箱自动设计系统v1.0
该示例代码仅供演示使用，其中参数请根据实际情况进行调整
建议放在 `.python` 目录下。
>前提条件：本程序需要已经安装rich和numpy库。

## 运行

以在 `.python` 为例：

```bash
cd D:/.code/.python/Gearbox-Automatic-Design-System
python main.py
```

## 文件结构

本程序结构如下：

```bash
.main.py
├── motor                   # 电动机的选择
├── gear_ratio              # 传动装置的总传动比及其分配
├── transmission_parameters # 计算传动装置的运动和动力参数
├── gear_drive              # 齿轮传动的设计计算
├──                         # 链传动设计
├── axis                    # 轴及联轴器和轴承的设计计算
├── rolling_bearing         # 滚动轴承的校核
├── key                     # 键的选择及强度校核
├── box_and_accessories     # 箱体设计及附属部件设计
├──                         # 润滑与密封
└── end_cap                 # 端盖设计
```
