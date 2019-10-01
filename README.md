pip3 install -r requirements.txt
# pra gerar o requirements.txt
pip3 freeze > requirements.txt

aws s3 mb s3://fernando.pimenta.com.br
aws s3 sync . s3://fernando.pimenta.com.br
aws rekognition create-collection --collection-id nome-da-colecao

# deletando ambiente para evitar custos
aws s3 rb s3://fernando.pimenta.com.br --force
aws rekognition delete-collection --collection-id faces

# s3 subir site
aws s3 rm s3://fernando.pimenta.site.com.br --recursive
aws s3 cp ./fa-site s3://fernando.pimenta.site.com.br --recursive --acl public-read
aws s3 cp teste.png s3://fernando.pimenta.site.com.br
# Cors
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration> 

# policy
{
    "Id": "Policy1569889808748",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1569889807410",
            "Action": [
                "s3:GetObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::fernando.pimenta.com.br/*",
            "Principal": "*"
        }
    ]
}

#subindo lambda
zip faceanalise.zip faceanalise.py
aws lambda update-function-code 
--function-name faceAnalise --zip-file fileb://faceanalise.zip

#publicando
aws lambda publish-version --function-name faceAnalise
aws lambda create-alias --function-name faceAnalise --function-version
1 --name PROD

