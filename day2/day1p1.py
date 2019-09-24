'''
将华氏温度转为摄氏度
anthor:daiyufen
version:0.1
'''
f = float(input('请输入华式温度值：'))
c = (f - 32) / 1.8
print('华氏度：%.1f = 摄氏度：%.1f '%(f,c))