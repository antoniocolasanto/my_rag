import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. CARICAMENTO CHIAVE API
load_dotenv()

# 2. CARICAMENTO DEI TESTI
# Questo caricherà TUTTI i file .txt presenti nella tua cartella
print("📖 Lettura dei file TXT in corso...")
loader = DirectoryLoader('./', glob="./*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
docs = loader.load()

if not docs:
    print("❌ Nessun file .txt trovato! Crea un file chiamato appunti.txt")
    exit()

print(f"✅ Caricati {len(docs)} file di testo.")

# 3. CREAZIONE DATABASE VETTORIALE
print("⏳ Creazione database in memoria...")
vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 3}) # Prende i 3 pezzi più rilevanti

# 4. CONFIGURAZIONE AI E PROMPT
template = """Rispondi alla domanda usando SOLO il contesto fornito:
{context}

Domanda: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Catena di esecuzione
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# 5. CHIEDI ALL'AI
print("\n--- SISTEMA PRONTO ---")
while True:
    domanda = input("\n❓ Cosa vuoi sapere dai tuoi appunti? (scrivi 'esci' per chiudere): ")
    if domanda.lower() == 'esci':
        break
    
    try:
        risposta = chain.invoke(domanda)
        print(f"\n🤖 RISPOSTA AI:\n{risposta}")
    except Exception as e:
        print(f"❌ Errore: {e}")