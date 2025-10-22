<p align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">RAG-AI</h1></p>
<p align="center">
<em><code>A simple and efficient Retrieval-Augmented Generation (RAG) system built with LangChain.</code></em>
</p>
<p align="center">
<img src="https://img.shields.io/github/license/abdebennar/rag-ai?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/abdebennar/rag-ai?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/abdebennar/rag-ai?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/abdebennar/rag-ai?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
<!-- default option, no dependency badges. -->
</p>
<br>

## Table of Contents

- [Overview](#overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
  - [Project Index](#-project-index)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Installation](#-installation)
  - [Usage](#-usage)
  - [Testing](#-testing)
- [Project Roadmap](#-project-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## Overview

RAG-AI is a Retrieval-Augmented Generation (RAG) system designed for efficient question-answering over custom documents.  
It leverages **LangChain** to integrate document loading, text splitting, embeddings, vector database creation (**ChromaDB**),  
and a large language model (**LLM**) from **Groq**.  

This project provides a straightforward way to build a RAG application for various data types,  
focusing on **Markdown files** in its current configuration.

---

## Features

- **Document Loading:** Efficiently load documents from a specified directory with support for multithreading.  
- **Text Splitting:** Intelligent text splitting using a HuggingFace tokenizer to ensure meaningful chunks for embeddings.  
- **Embeddings:** Utilizes `HuggingFaceEmbeddings` with `sentence-transformers/all-MiniLM-L6-v2` for generating document embeddings, supporting both CPU and CUDA devices.  
- **Vector Database:** Persists and retrieves document chunks using **ChromaDB**.  
- **RAG Chain:** Integrates a retrieval chain with a **Large Language Model (LLM)** from Groq (specifically `llama-3.3-70b-versatile`) for contextual question answering.  
- **Interactive CLI:** Provides a command-line interface for asking questions and receiving answers from the RAG system.  
- **Automated Dependency Installation:** The `install.sh` script automatically detects and installs missing Python modules and updates `requirements.txt`.

---

## Project Structure

```sh
└── rag-ai/
    ├── README.md
    ├── __pycache__
    │   └── config.cpython-310.pyc
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── main.py
    ├── config.py
    ├── install.sh
    ├── requirements.txt
    └── scripts
        ├── __init__.py
        ├── __pycache__
        ├── chain.py
        ├── chroma.py
        ├── embeddings.py
        ├── loader.py
        ├── prompt.py
        └── splitter.py
```
