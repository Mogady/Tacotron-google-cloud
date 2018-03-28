# Tacotron

An implementation of Tacotron speech synthesis in TensorFlow configured to run on google cloud machine learning engine.
this is the same implementation here [Tacotron](https://github.com/keithito/tacotron) but changed a little to run on google ML Engine
please refer to the linke above for source implementation details and how it works

## changed args
**--Output_dir**
	this is replacement for --base_dir where you define the cloud storage path to your ouput directory
	
**--input**
	here you define the path to your bucket on cloud storage where you have training data (train.txt)
	```
	ex: gs://BUCKET_NAME/training/train.txt
	```



