# FSM_RPG
## Index
1. Introduction
2. Structure
3. TODO & Doing
## Introduction
自制python包，基本设定基于DND五版规则书，感谢*纯美苹果园*提供的中文资料，DND真的很有趣
## Structure
pyfsm包结构目前如下：
+ Action(角色怪物的动作行为函数生成类，包括基础通用的函数)
+ Error(自定义的一些异常)
+ Generator(角色，怪物的生成器，通过json文件)
+ Helper(自定义的辅助函数，辅助类)
+ json(角色，怪物的定义文件)
+ Machine(角色和怪物的基础类)
+ State(角色和怪物的状态生成类)
+ System(世界，系统生成运行类)
## TODO & Doing
python:目前主要在制作的是关于基础战斗轮的部分
html&js:html目前只做到攻击和法术，roll属性只做了3d6，js目前亟需完善种族角色背景等相关的内容
