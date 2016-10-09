def hexdump(c):
	length = 16;
	for i in xrange(0, len(c), length):
		s1 = c[i : i + length]
		s2 = ' '.join(["%02x" % ord(x) for x in s1]);
		s2 = ' '.join([s2[:24], s2[24:]])
		l = []
		for j in s1:
			if ord(j) > 32 and ord(j) < 127:
				l.append(j)
			elif ord(j) == 32:
				l.append(' ')
			else:
				l.append('.')
		s3 = ''.join([x for x in l])
		print "%08x:  %-48s  |%s|" % (i, s2, s3)

fileName = raw_input()
try:
	f = open(fileName, 'rb')
	hexdump(f.read())
except Exception:
	print "Cannot open the file 'filename'" 