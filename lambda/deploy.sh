mkdir lib
mkdir dist

zip -r dist/deployment.zip ./lib/*
zip -g dist/deployment.zip service.py
aws lambda update-function-code --function-name MovieRecommendation --zip-file fileb://dist/deployment.zip
