#!/bin/bash
set e

#run the document ingestion(one-time)
python -m src.rag_doc_ingestion.ingest_docs

# start backend fastapi
uvicorn src.backend_src.main:app --host 0.0.0.0 --port 8000 &

#start frontend streamlit
streamlit run src/frontend_src/app.py --server.port 8501 --server.address 0.0.0.0



