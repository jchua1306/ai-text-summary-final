from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from typing import Optional

# Initialize the FastAPI app
app = FastAPI(title="Text Summarization API", 
              description="API for summarizing text using BART Large CNN model",
              version="1.0.0")

# Load the summarization model
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

# Create a request model
class SummarizationRequest(BaseModel):
    text: str
    max_length: Optional[int] = 130
    min_length: Optional[int] = 30
    do_sample: Optional[bool] = False

# Create a response model
class SummarizationResponse(BaseModel):
    summary: str

@app.post("/summarize/", response_model=SummarizationResponse)
async def summarize_text(request: SummarizationRequest):
    """
    Summarize the input text using the BART Large CNN model.
    
    - **text**: The text to summarize
    - **max_length**: Maximum length of the summary (default: 130)
    - **min_length**: Minimum length of the summary (default: 30)
    - **do_sample**: Whether to use sampling (default: False)
    """
    try:
        # Check if text is too short
        if len(request.text.split()) < 10:
            raise HTTPException(status_code=400, detail="Text is too short for summarization")
            
        # Generate summary
        result = summarizer(
            request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=request.do_sample
        )
        
        # Extract summary from result
        summary = result[0]['summary_text']
        
        return SummarizationResponse(summary=summary)
    
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Text Summarization API. Use /summarize/ endpoint to summarize text."}

# If running the file directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)