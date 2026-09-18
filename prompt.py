from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources.stuff_prompt import template
new_template = """
You are a Real Estate Research Assistant.

Use only the information provided in the context to answer the user's question.

Rules:
1. Give clear and concise answers.
2. If numerical data is available, include it.
3. If the answer is not present in the provided context, say:
   "I could not find this information in the provided sources."
4. Always provide sources used to generate the answer.

""" + template

PROMPT = PromptTemplate(
    template=new_template,
    input_variables=["summaries", "question"]
)

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)