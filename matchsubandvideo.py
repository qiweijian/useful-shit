 #!/usr/bin/python 
 # -*- coding: utf-8 -*
import os

def matchVideoName(path, showName, matchindex):
	total_list = os.listdir(path)
	for i in total_list:
		newname = showName + ' - s01e' + i[matchindex] + '.mkv'
    	print(newname)
    	os.rename(i,newname)

def matchSubName(path, videoindex, videoext, subindex, subext):
	total_list = os.listdir(path)
	video_dict = {}
	sublist = list()
	for i in total_list:
		if os.path.splitext(i)[1] == videoext:
			video_dict[i[videoindex:videoindex+2]] = i
		if os.path.splitext(i)[1] == subext:
			sublist.append(i)
	for i in sublist:
		subnumber = i[subindex:subindex+2]
		newname = video_dict[subnumber]
		newname = os.path.splitext(newname)[0]+subext
		print(newname)
		os.rename(os.path.join(path,i),newname)

if __name__ == '__main__':
	pathname = '/Volumes/Multimedia/Videos/TVseries/Prison.Break'
	matchSubName(pathname,17,'.mkv',17,'.ass')
        	

