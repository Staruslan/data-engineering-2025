import pandas as pd
import requests
from io import StringIO
#https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=drive_link

FILE_ID = "1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq"
file_url = f"https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=drive_link={FILE_ID}"

response = requests.get(file_url)
raw_data = pd.read_csv(StringIO(response.text))
print(raw_data.head(10))
