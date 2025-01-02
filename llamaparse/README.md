# Llamaparse 

## Setup
1. Clone the repo and navigate to the folder
    ```
    git clone https://github.com/sudarshan-koirala/youtube-stuffs.git
    cd youtube-stuffs
    cd llamaparse
    ```

2. Make sure you have `uv` installed,
    - If not installed, here is the website [link](https://docs.astral.sh/uv/getting-started/installation/)
    - Refer to my [Youtube video](https://youtu.be/13eNodHGRjw?si=zvw4fMn2wZ7DGd_V) if any assistance needed.

3. Install the necessary packages, it also creats the virtual environment for you.
    ```
    uv sync
    ```

4. Provide environment variables from [llamacloud](https://cloud.llamaindex.ai/project/98f145ce-812c-4f7c-9a0c-c6b51993a12b/api-key) and [groq](https://console.groq.com/keys) in the `.env` file.
    - Rename `.env.example` to `.env`
    - Provide your env variables inside it
    ```
    LLAMA_CLOUD_API_KEY="llx-xxxxxxxxxxx"
    GROQ_API_KEY="gsk_xxxxxxxx"
    ```

4. Follow along with me in the `llamaparse.ipynb` file.

That's it. Happy learning 😎