from selenium import webdriver


class Bot:
	def __init__(self):
		self.start()
	
	def start(self):
		web = webdriver.Chrome()
		web.get("https://10fastfingers.com/typing-test/turkish")
		for i in range(1, 292):
			text = web.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) + ']').text
			inputt = web.find_element_by_xpath('//*[@id="inputfield"]')
			inputt.send_keys(text + " ")


Bot()
