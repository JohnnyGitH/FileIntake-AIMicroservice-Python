from fastapi import APIRouter
from app.services import summarize_document, eli5_document, pointform_document
from app.models import SummaryRequest, SummaryResponse

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize(req: SummaryRequest):
    print("🔥 summarize endpoint hit")
    print("📦 request: ", req)
    result = await summarize_document(req.text)
    return SummaryResponse(summary=result)

@router.post("/eli5", response_model=SummaryResponse)
async def eli5(req: SummaryRequest):
    print("🔥 explain like I am 5 endpoint hit")
    print("📦 request: ", req)
    result = await eli5_document(req.text)
    return SummaryResponse(summary=result)

@router.post("/pointform", response_model=SummaryResponse)
async def pointform(req: SummaryRequest):
    print("🔥 explain like I am 5 endpoint hit")
    print("📦 request: ", req)
    result = await pointform_document(req.text)
    return SummaryResponse(summary=result)