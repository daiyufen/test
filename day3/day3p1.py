'''
英寸和厘米厘米互换
version:0,1
author:小雨
'''
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.1f英寸 = %.1f厘米' % (value, 2.54 * value))
elif unit == 'cm' or unit == '厘米':
    print('%.1f厘米 = %.1f英寸' % (value, value / 2.54))
else:
    print('请输入正确单位')
