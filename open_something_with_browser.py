import webbrowser

def openSomething(link):
	'''opens a link'''
	try:
		url = f"www.{str(link.lower())}.com"#formats to a typical  address
		if "http" in link:#if complete link is provided
			x = webbrowser.open(link)
		elif "." in link:#if a non http link is given
			x = webbrowser.open(link)

		elif "https" not in link:#only name is specified
			x = webbrowser.open(url)
		return x
	except Exception :
		return "Error ocurred"


print(openSomething("google"))
