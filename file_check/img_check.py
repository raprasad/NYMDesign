import os, sys
import stat

img_data_fname = 'img_list.txt'
img_src_dir = '../static_media/media'

def check_images():
	img_names = open(img_data_fname, 'r').readlines()
	#print len(img_names)
	img_names = [x.strip() for x in img_names if len(x.strip()) > 0]
	#print len(img_names)
	#img_names = filter(lambda x: len(x)>0, img_names)

	cnt = 0
	not_found = []
	too_small = []
	for img_name in img_names:
		cnt += 1 
		print('(%s) checking: %s' % (cnt, img_name))
		fpath = os.path.join(img_src_dir, img_name)
		if not os.path.isfile(fpath):
			not_found.append(img_name)
		else:
			fsize = os.stat(fpath)[stat.ST_SIZE]
			if fsize < 10:
				too_small.append(img_name)
				
	print len(not_found)
	not_found.sort()
	print '\n'.join(not_found)
	#	print not_found
	print len(too_small)

if __name__=='__main__':
	check_images()