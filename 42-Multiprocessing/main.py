import multiprocessing
import requests
import concurrent.futures 


def downloadFile(url, i):
    print(f"Downloading started for {i}")
    response = requests.get(url)
    open(f"image{i}.jpg","wb").write(response.content)
    print(f"Downloading Done for {i}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    # pros = []
    # for i in range(6):
    #     # downloadFile(url, i)
    #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [i for i in range(5)]
        l2 = [url for i in range(5)]
        results = executor.map(downloadFile, l2, l1)
        # for r in results:
        #     print(r)