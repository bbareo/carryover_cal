# 补偿时间轴计算
适用于Hoshino的公主连结R会战补偿时间轴计算器。

## 概览
- 通过完整时间轴，转换出返还20~89秒时间后的对应轴。
- 指令格式：`转秒 <返还时间> <时间轴>`<br>其中`<返还时间>`和`<时间轴>`之间、`<时间轴>`的每行之间，都**必须换行**。
- **可接受**的秒数格式举例：以`65秒`为例，`065`，`65s`，`105`，`1:05`，`01：05`等均可。
- **无法识别**的秒数格式举例：以`65秒`为例，`1:5`，`1：5`等均不可。

## 使用方法
1. 克隆或下载本项目，放置于`HoshinoBot/hoshino/modules`目录下：

```
git clone https://github.com/bbareo/carryover_cal
```

3. 在`HoshinoBot/hoshino/config/__bot__.py`文件的`MODULES_ON`中添加值`carryover_cal`
4. 重启Hoshino

## 使用举例
<img src="https://raw.githubusercontent.com/bbareo/carryover_cal/main/20230301225446.png" width=60% title="example">

## 待更新
当时间前有任何非空字符时，将不进行转换。<br>
目的是为了避免技能中含有数字（如“TA3”、“リンケージ２段”等）时，会被匹配并参与转换。<br>
但这样会导致在操作被括号包裹等特殊情况下，该行时间将不被转换，如图所示：
<img src="https://raw.githubusercontent.com/bbareo/carryover_cal/main/20230301225454.jpg" width=60% title="err_eg">
