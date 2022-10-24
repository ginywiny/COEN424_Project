mkdir dist
rm dist/deployment.zip

#zip -q -r dist/deployment.zip ./../env/lib/python3.10/site-packages/*
zip -g dist/deployment.zip lambda_function.py
aws lambda update-function-code --function-name MovieRecommendation --zip-file fileb://dist/deployment.zip
