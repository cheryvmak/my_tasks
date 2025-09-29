
# To import from google drive
''' pip install gdown
url = 'htt..'
id = 'after the file/d/ which start from digit'
df = gd.download(f"https://drive.google.com/uc?id={id}, quiet = False)
df = pd.read_csv('')
df2 = df.copy()

# To import from wikipedia.
import requests
url = ''
headers = {"user.Agent": "Mozilla/5.0"}
response = requests.get(url,  headers = headers)
country = pd.read_html()




 from kaggle 

step1: Install kagglehub using
pip install kagglehub
Step2: import kagglehub in notebook
import kagglehub
Step 3: Download dataset
path = kagglehub.dataset_download("abrambeyer/openintro-possum")
Step4: Print Dataset path(optional)
print("Path to dataset files:", path)
'''


