pip3 install -r requirements.txt
# pra gerar o requirements.txt
pip3 freeze > requirements.txt

aws s3 sync . s3://fernando.pimenta.com.br
aws rekognition create-collection --collection-id nome-da-colecao
