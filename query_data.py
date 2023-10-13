from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAIChat
from langchain.chains import ChatVectorDBChain

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
You can assume the question is about companies whose data is HTML format. You should answer these questions in English by finding data
in HTML and translating to English.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """You are an AI assistant for answering questions about companies whose data is in HTML format.
You are given the following extracted parts of a long HTML document and a question. Provide a conversational answer.
If you don't know the answer, just say "Hmm, I'm not sure." Don't try to make up an answer.
If the question is not about a company whose data is in HTML format, politely inform them that you are tuned to only 
answer questions about companies whose data is in HTML format.
Question: {question}
=========
{context}
=========
Answer in Markdown:"""
QA_PROMPT = PromptTemplate(template=template, input_variables=["question", "context"])


def get_chain(vectorstore):
    llm = OpenAIChat(temperature=0)
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain
