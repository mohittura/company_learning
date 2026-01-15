from os import environ
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Read allowed origins from the environment variable `ALLOWED_ORIGINS` (comma-separated).
# Example
origins_env = environ.get("ALLOWED_ORIGINS")
if origins_env:
   origins = [o.strip() for o in origins_env.split(",") if o.strip()]
else:
   origins = [
      "http://localhost",
      "http://localhost:8080",
      "http://mohit.gov.us"
   ]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

@app.get("/")
async def main():
   return {"message": "Hello World"}

@app.get("/cors-origins")
def cors_origins():
   """Return the active allowed origins (useful for debugging)."""
   return {"allowed_origins": origins}