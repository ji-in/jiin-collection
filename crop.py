import dlib, cv2, glob

face_detector = dlib.get_frontal_face_detector()

path = glob.glob("./data/celeb/*.jpg") # 크롭할 이미지가 있는 폴더 경로
cv_img = list()
count = 1
for img in path:
    
    image = cv2.imread(img)
    faces = face_detector(image)
    print("얼굴검출을 완료했습니다.")
    
    for f in faces:
        left = f.left()
        right = f.right()
        top = f.top()
        bottom = f.bottom()
        
        crop = image[top:bottom, left:right]
        try:
            cv2.imwrite("./data/celeb_crop/" + str(count) + ".jpg", crop) # 이미지 저장하기 위한 폴더 경로
        except:
            pass
    print("Crop 이미지 저장을 완료했습니다.")
    
    count += 1