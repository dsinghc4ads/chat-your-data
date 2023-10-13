from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)

response = index.query("What is the Investment Corporation of Bangladesh?")
print(response)