import cv2
import face_recognition
import pickle
import  os

#importando as fotos dos estudante
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []


for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    #divide o codigo em duas partes removendo o .png do codigo do aluno
    studentIds.append(os.path.splitext(path)[0])
    #print(path)

print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started. . .")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithids = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithids, file)
file.close()
print("Arquivos salvos")

