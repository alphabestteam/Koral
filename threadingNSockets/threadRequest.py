import requests
import time
import threading


def download_file(url: str, name_of_file: str) -> None:
    with open(name_of_file + ".jpg", "wb") as fd:
        fd.write((requests.get(url)).content)


def timer(func):
    def inner(*args, **kwargs) -> int:
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"it took {end - start:0.4f} seconds to download")
    return inner
    
@timer
def main():
    list_of_urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png", "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png", "https://github.githubassets.com/images/modules/open_graph/github-mark.png", "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"]
    list_of_thread = []
    count = 0

    for i in list_of_urls:
    
        thread = threading.Thread(target=download_file, args=(i, f"file{count}"))
        list_of_thread.append(thread)
        count +=1 

    for threads in list_of_thread:
        threads.start()

if __name__ == "__main__":
    main()