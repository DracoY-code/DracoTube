import apiclient.discovery as api
from pytube import YouTube

import webbrowser

# Get api key from text file
with open(r"resources\apiKEY.txt") as f:
    API_KEY = f.readline().rstrip()

# Build YouTube object
YT = api.build('youtube', 'v3', developerKey=API_KEY)


def addId(object, index=0):
    """ Append search video id in list for further use. """
    global idList, nameList
    video_id = object[index]['id']['videoId']
    idList.append(video_id)


def get_url(id: str):
    """ Converts video id into url for the video. """
    url = "https://youtu.be/" + id
    return url


def download_video(url: str, title: str):
    """ Download the video through url. """
    try:
        YouTube(url).streams.first().download('downloads', filename=title)
    except:
        print("Connection Error!")
    # Can get audio too by get_audio_only(subtype: str = 'mp4')


def erase():
    """ The dumpster to erase earlier searches. """
    idList.clear(); nameList.clear()


# -----------------------------------------------------------------------------
print("\nWelcome to DracoTube App V01\n"
      + "<YouTube Terminal Application>\n")

while True:
    print("Hello friend!\n"
          + "What do you wanna do?\n\n"
          + "0 - Search a video\n"
          + "1 - Exit the app\n")
    choice = input("Your choice: ")
    print()

    # Video search
    if choice == "0":
        # Containers
        idList = []
        nameList = []

        while True:
            # Search video based on keyword
            query = input("Search YouTube video (x to exit): ")
            if query == "x":
                erase()
                break
            limit = input("Set search limit: ")
            print()

            # Get search results
            try:
                request = YT.search().list(
                    q=query, part='snippet', type='video',
                    maxResults=limit, pageToken=None
                )
            except:
                print("Invalid search!")
                break
            results = request.execute()
            results = results['items']

            # Display search results
            number_of_results = len(results)
            print(f"#Results for {query}")
            for a in range(number_of_results):

                search = results[a]['snippet']
                channel_name = search['channelTitle']
                title = search['title']

                nameList.append(title)
                addId(results, a)

                print(f"{a} -- {title} <{channel_name}>")
            print()

            while True:
                # Ask user to perform an action (choose video)
                code = input("Select video code (x to go back): ")
                if code == "x":
                    # Dumpster
                    erase()
                    print()
                    break
                print()

                print("Ok, what's your plan now?\n"
                      + "0 - Open the video\n"
                      + "1 - Download the video\n"
                      + "2 - Go back!")
                option = input("::? ")
                if option not in ['0', '1', '2']:
                    print("\nInvalid choice!\n")
                    erase()
                    break
                print()

                # Open video
                if option == "0":
                    try:
                        url = get_url(idList[int(code)])
                        webbrowser.open(url)
                        print("Enjoy your video!\n")
                    except:
                        print("Error while loading page!\n")
                        break
                    finally:
                        erase()

                # Download video
                if option == "1":
                    try:
                        url = get_url(idList[int(code)])
                        downloadTitle = nameList[int(code)]
                        download_video(url, downloadTitle)
                        print("Congrats! Your download should be ready.\n")
                    except:
                        print("Error while downloading!\n")
                        break
                    finally:
                        erase()

                # Go back to main console
                if option == "2":
                    erase()
                    break

    # End the program
    if choice == "1":
        print("See you later!")
        break

    print()
# -----------------------------------------------------------------------------
