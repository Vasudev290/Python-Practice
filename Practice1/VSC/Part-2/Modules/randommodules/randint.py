from random import *
#dir(random)
#print(dir(random))

'''
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', 
'_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', 
'_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', 
'_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 
'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 
'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
'''
'''
1.print 10 random number rangw between 10 to 99
  #randint function => To generate random integer between given numbers
'''
for i in range(10):
    print(randint(10,100)) #19,72,69,100,22,54,74,87,78.67