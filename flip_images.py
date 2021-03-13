import cv2, os

def flip_images():
	gest_folder = "data"
	g_id="train"
	f=0
	#images_labels = []
	#images = []
	#labels = []
	for g_id in os.listdir(gest_folder):
		for f in range(10):
			for i in range(0,500,1):
				path = gest_folder+"/"+g_id+"/"+str(f)+"/"+str(i+1)+".jpg"
				new_path = gest_folder+"/"+g_id+"/"+str(f)+"/"+str(i+1+500)+".jpg"
				print(path)
				print(new_path)
				img = cv2.imread(path, 0)
				img = cv2.flip(img, 1)
				cv2.imwrite(new_path, img)
			#f=int(f)+1

flip_images()
