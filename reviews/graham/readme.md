have reformatted the data according to their baseline.py script, which they claim was used to achieve the [baseline result of 3.17](https://www.kaggle.com/c/pkdd-15-predict-taxi-service-trajectory-i/forums/t/13568/beating-the-benchmark
)

I believe I’m following what their baseline.py script does, both in terms of reformatting the polyline data and creating the model. My only difference is that I am using a separate process to extract the features from the polyline string, which are then stored in new training and testing files. I’m doing it this way in order to save time and memory usage.

However, my results so far are no where near the baseline result!

Could you please help?