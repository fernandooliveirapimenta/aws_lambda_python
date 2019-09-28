import boto3
import json

client = boto3.client('rekognition')
s3 = boto3.resource('s3')

def detecta_faces():
    faces_detectadas=client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'fernando.pimenta.com.br',
                'Name': '_analise.png'
            }
        },
    )
    return faces_detectadas

def cria_lista_faceId_detectadas(faces_detectadas):
    faceId_detectadas = []
    for i in range(len(faces_detectadas['FaceRecords'])):
        faceId_detectadas.append(faces_detectadas['FaceRecords'][i]['Face']['FaceId'])
    return faceId_detectadas

faces_detectadas = detecta_faces()
faceId_detectadas = cria_lista_faceId_detectadas(faces_detectadas)
print(faceId_detectadas)
# print(json.dumps(faces_detectadas))