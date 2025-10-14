## Progress
Currently have two SERP APIs connected to mcphost
1. DuckDuckGo
2. Serper API (google search)

## Project Structure

```
llm-mcp-ura/
├── servers/
│   └── serp-mcp/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── server.py
└── local.json
```

Ignore the files not listed above 

## Instructions

Sign up at https://serper.dev/playground for the Serper API (Google Search) key.
DuckDuckGo doesn't need an API key.

Either insert API key in ENV SERPER_API_KEY="INSERT_UR_OWN_API_KEY_HERE_PLZ" for Dockerfile
or, better,

delete ENV SERPER_API_KEY="INSERT_UR_OWN_API_KEY_HERE_PLZ" in Dockerfile and create a .env so that

```
llm-mcp-ura/
├── servers/
│   └── serp-mcp/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── server.py
│       └── .env
└── local.json
```

and add SERPER_API_KEY="INSERT_UR_OWN_API_KEY_HERE_PLZ" in .env
