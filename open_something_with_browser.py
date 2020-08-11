import webbrowser

def openSomething(link):
	url = f"www.{str(link.lower())}.com"
	x = webbrowser.open(url)
	return x


print(openSomething("youtube"))
