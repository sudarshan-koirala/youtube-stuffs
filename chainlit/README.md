# Chainlit

## Setup
1. Clone the repo and navigate to the folder
    ```
    git clone https://github.com/sudarshan-koirala/youtube-stuffs.git
    cd youtube-stuffs
    cd chainlit
    ```

2. Make sure you have `uv` installed,
    - If not installed, here is the website [link](https://docs.astral.sh/uv/getting-started/installation/)
    - Refer to my [Youtube video](https://youtu.be/13eNodHGRjw?si=zvw4fMn2wZ7DGd_V) if any assistance needed.

3. Install the necessary packages, it also creats the virtual environment for you.
    ```
    uv sync
    ```

4. We will use Qdrant locally, so lets provide qdrant url in the `.env` file.

    TO RUN QDRANT LOCALLY, INSTALL [DOCKER](https://www.docker.com/get-started/) FIRST, HERE IS THE [LINK](https://qdrant.tech/documentation/quickstart/)
    ```
    docker pull qdrant/qdrant
    docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
    
    ```
    - Rename `.env.example` to `.env`
    - Provide your env variables inside it as shown below.
    ```
    QDRANT_URL_LOCALHOST="xxxxx"
    ```
    - If you need more info about Qdrant, refer to the [ths video](https://youtu.be/JSKZYgARffg?si=0Jf7jxfMYzrPR0w5) I created about Qdrant.

4. Run the chainlit app
    ```
    uv run ingest.py
    uv run chainlit run rag-chainlit-deepseek.py
    ```

    
5. For more info follow along with me in the video.

---
Important Links:
- https://ds4sd.github.io/docling/examples/rag_langchain/
- https://blog.gopenai.com/how-to-build-a-chatbot-to-chat-with-your-pdf-9abb9beaf0c4

 Happy learning 😎