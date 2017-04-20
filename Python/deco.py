def logger(function):
	def intern(*args,**kwargs):
		print('arg sent:')
		print('args : {}'.format(args))
		print('kwargs : {}'.format(kwargs))
	print('decorating function:',function.__name__)
	return intern

@logger					# decorate the following function - call logger() on it
def test_fct(val1,val2,val3):
	print('test')

test_fct(1,'allo',val3=2)



