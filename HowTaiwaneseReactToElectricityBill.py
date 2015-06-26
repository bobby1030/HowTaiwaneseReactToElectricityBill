# encoding: utf-8
import time



i = 1
def ZH():
	while i > 0:
		Policy = str(input('政府政策(電費調漲:UP,節電獎勵:DOWN,維持現狀:HOLD)：'))
	
		if Policy.lower() == 'up':
			React = '民不聊生'
		elif Policy.lower() == 'down':
			React = '降價無感'
		elif Policy.lower() == 'hold':
			React = '政府無能'
		else:
			print('   ','輸入錯誤')
			ZH()

		print('民眾反應：')
		print('     '+React+'!')
		time.sleep(0.3)
		print('     '+React+'!!')
		time.sleep(0.3)
		print('     '+React+'!!!')
		time.sleep(0.3)
		print('     '+React+'!!!!')
		time.sleep(0.3)
		print('     '+React+'!!!!!')
		time.sleep(0.3)
		print('')

def EN():
	while i > 0:
		Policy = str(input('If Electricity Bill Goes UP,DOWN,or HOLD:'))
	
		if Policy.lower() == 'up':
			React = 'People have no way of making a living'
		elif Policy.lower() == 'down':
			React = 'No Feeling'
		elif Policy.lower() == 'hold':
			React = 'Government is powerless'
		else:
			print('   ','Input Error')
			EN()

		print('Taiwanese React:')
		print('     '+React+'!')
		time.sleep(0.3)
		print('     '+React+'!!')
		time.sleep(0.3)
		print('     '+React+'!!!')
		time.sleep(0.3)
		print('     '+React+'!!!!')
		time.sleep(0.3)
		print('     '+React+'!!!!!')
		time.sleep(0.3)
		print('')

#詢問語言

Lang = str(input('Please Choose A Language,EN or ZH\n請選擇語系,中文輸入:ZH,英文輸入:EN：'))

if Lang.lower() == 'en':
	EN()
if Lang.lower() == 'zh':
	ZH()