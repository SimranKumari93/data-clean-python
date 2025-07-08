# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("arianazmoudeh/airbnbopendata")

# print("Path to dataset files:", path)

import kagglehub 
# kagglehub.login(path_to_kaggle_json="path/to/kaggle.json")

path = kagglehub.dataset_download("arianazmoudeh/airbnbopendata")
print("Path to dataset files:", path)
