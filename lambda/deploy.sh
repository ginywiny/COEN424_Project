mkdir lib
mkdir dist

pip3 freeze > requirements.txt
pip3 install -r requirements.txt --target ./lib
zip -r dist/deployment.zip ./lib/*
zip -g dist/deployment.zip service.py
aws lambda update-function-code --function-name MovieRecommendation --zip-file fileb://dist/deployment.zip
