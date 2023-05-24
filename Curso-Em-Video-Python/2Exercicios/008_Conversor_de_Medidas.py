m = float(input('Uma distancia em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {} corresponde :'.format(m))
print(' Km= {}\n hm= {}\n dam= {}\n dm= {:.0f}\n cm= {:.0f}\n mm= {:.0f}'.format(km, hm, dam, dm, cm, mm))