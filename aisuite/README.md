# Aisuite 

## Setup
1. Check python version, for me it is `Python 3.11.0` by running `python3 --version`. I assume you have python installed, if not please it first.
2. Create virtual environment and activate it `python3 -m venv .venv && source .venv/bin/activate`
3. Install sll the provider-specific libraries `pip install 'aisuite[all]'`

### With Ollama
Please install Ollama if you don't have already.  
- [Official website link](https://ollama.com/)
- [Playlist of Ollama](https://youtube.com/playlist?list=PLz-qytj7eIWX-bpcRtvkixvo9fuejVr8y&si=S4sHAFkzLVleuuIS)  

- Check if Ollama is installed, type `ollama` in your terminal.
- If you run it manually, no need to run `ollama serve` as it will be already running.
- If not triggered manually, run `ollama serve` in the terminal.

Once you run, check it is listeninig in the port it should be [running](http://127.0.0.1:11434)