# mkdir dist
rm dist/deployment.zip
zip -gr dist/deployment.zip zip ml-100k/ model/ data.py inference.py lambda_function.py model.py train.py utils.py
aws lambda update-function-code --function-name MovieRecommendation --zip-file fileb://dist/deployment.zip