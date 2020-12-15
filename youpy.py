import webbrowser
u='http://www.youtube.com'

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
c=webbrowser.get('chrome')

c.open(u)
