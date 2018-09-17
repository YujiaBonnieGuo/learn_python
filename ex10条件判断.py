# age=2
# print('your age is',age)
# if age>=18:
#     print('adult')
# elif age>=6:
# 	print('tennager')
# else:
# 	print('kid')

hight=float(input('请输入身高（单位：米）：'))
weight=float(input('请输入体重（单位：千克）：'))
# BMI=weight/(hight*hight)
BMI=weight/(hight**2)
if BMI<18.5:
	print('过轻')
elif BMI<25:
	print('正常')
elif BMI<28:
	print('过重')
elif BMI<32:
	print('肥胖')
else:
	print('严重肥胖')
    
H = float(input('请输入身高（单位：米）：'))

W = float(input('请输入体重（单位：公斤）：'))

bmi = W/(H**2)

if bmi >=32:
    print('你的BMI指数%.1f,严重肥胖'% BMI)
elif bmi>=28:
    print('你的BMI指数%.1f,肥胖'% BMI)
elif bmi>=25:
    print('你的BMI指数%.1f,过重'% BMI)
elif bmi>=18.5:
    print('你的BMI指数%.1f,正常'% BMI)
elif bmi>0:
    print('你的BMI指数%.1f,过轻'% BMI)
else:
    print('输入有误')