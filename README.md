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
	
### Code changes

**DataFeeder.py**:
	1. at _init_ function change
		```
		with open(metadata_filename, encoding='utf-8') as f:
		```
		To
		```
		with file_io.FileIO(metadata_filename, 'r') as f:
		```
		to make the model able to read gs paths

	2. at _get_next_example function:
		```
		linear_target = np.load(os.path.join(self._datadir, meta[0]))
		mel_target = np.load(os.path.join(self._datadir, meta[1]))
		```
		TO
		```
		f = BytesIO(file_io.read_file_to_string(
            os.path.join(self._datadir, meta[0]),binary_mode=True))
        linear_target = np.load(f)
        s = BytesIO(file_io.read_file_to_string(
            os.path.join(self._datadir, meta[1]),binary_mode = True))
        mel_target = np.load(s)
		```
		to read .npy files from gs paths
		*please refer to this [Answer](https://stackoverflow.com/questions/41633748/load-numpy-array-in-google-cloud-ml-job) to understand why 


