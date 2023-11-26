import webbrowser
from openai import OpenAI

# 使用瀏覽器開啟圖片
# url (str): 圖片的網址
def open_image_in_browser(url):
    webbrowser.open(url)

# 建立 OpenAI 的 client
client = OpenAI(api_key="_________👉YOUR_API_KEY___________")

# 產生圖片
response = client.images.generate(
    model="dall-e-3",
    prompt="麥當勞的美味漢堡",
    size="1024x1024",
    n=1,
)

# 取得圖片的網址
image_url = response.data[0].url
# 使用瀏覽器開啟圖片
open_image_in_browser(image_url)
