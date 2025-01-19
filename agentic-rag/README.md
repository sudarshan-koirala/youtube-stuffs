# Llamaparse 

## Setup
1. Clone the repo and navigate to the folder
    ```
    git clone https://github.com/sudarshan-koirala/youtube-stuffs.git
    cd youtube-stuffs
    cd agentic-rag
    ```

2. Make sure you have `uv` installed,
    - If not installed, here is the website [link](https://docs.astral.sh/uv/getting-started/installation/)
    - Refer to my [Youtube video](https://youtu.be/13eNodHGRjw?si=zvw4fMn2wZ7DGd_V) if any assistance needed.

3. Install the necessary packages, it also creats the virtual environment for you.
    ```
    uv sync
    ```

4. Provide environment variables from [openai](https://platform.openai.com/settings/organization/api-keys). If you use Qdrant cloud, then here is the link -> [Qdrant Cloud](https://cloud.qdrant.io/) in the `.env` file.
    - Rename `.env.example` to `.env`
    - Provide your env variables inside it as shown below.
    ```
    OPENAI_API_KEY="xxxxx"
    QDRANT_URL="xxxxx"
    QDRANT_API_KEY="xxxxx"
    QDRANT_URL_LOCALHOST="xxxxx"
    ```
    - If you need more info about Qdrant, refer to the [ths video](https://youtu.be/JSKZYgARffg?si=0Jf7jxfMYzrPR0w5) I created about Qdrant.

    IF YOU WANT TO RUN QDRANT LOCALLY, INSTALL [DOCKER](https://www.docker.com/get-started/) FIRST, HERE IS THE [LINK](https://qdrant.tech/documentation/quickstart/)
    ```
    docker pull qdrant/qdrant
    docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
    
    ```
4. Follow along with me in the video.

## Agentic RAG Advantages

Agentic Retrieval-Augmented Generation (RAG) combines intelligent agents with retrieval-augmented generation to enhance data retrieval and decision-making processes. Here’s a simplified overview of its key advantages:
- Improved Reasoning for Better Responses: Agentic RAG enhances the reasoning capabilities of AI systems, leading to more accurate and contextually relevant responses.    ￼
- Smart Tool Selection Based on Queries: It enables intelligent agents to choose the most appropriate tools or data sources, such as knowledge bases or search engines, based on the context of a query.
- Integrated Memory for Context Awareness: By integrating memory, Agentic RAG allows AI systems to remember and utilize previous interactions, improving context awareness and continuity in conversations. ￼
- Effective Task Planning and Breakdown: The system can decompose complex tasks into manageable sub-tasks, enabling better planning and execution by the AI agents. ￼
- Seamless Integration with Various Data Sources: Agentic RAG offers flexibility in connecting with diverse data sources, including PDFs, websites, CSV files, and documents, enhancing its versatility across different applications. ￼

These features collectively make Agentic RAG a powerful approach for optimizing data retrieval and decision-making in AI systems.

That's it. Happy learning 😎