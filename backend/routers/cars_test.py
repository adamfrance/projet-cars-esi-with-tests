from math import ceil
from typing import List, Optional
from fastapi import APIRouter, Request, Body, BackgroundTasks
from models import CarBase

router = APIRouter()

@router.get("/all", response_description="List all cars")
async def list_all_cars(
    request: Request,
    min_price: int = 0,
    max_price: int = 100000,
    brand: Optional[str] = None,
    page: int = 1,
) -> dict:
    RESULTS_PER_PAGE = 25
    skip = (page - 1) * RESULTS_PER_PAGE
    
    query = {"price": {"$lt": max_price, "$gt": min_price}}
    if brand:
        query["brand"] = brand
        
    # count total docs - sans await pour mongomock
    count = request.app.mongodb["cars"].count_documents(query)
    pages = ceil(count / RESULTS_PER_PAGE)
    
    # Utilise la méthode find sans await pour mongomock
    cursor = request.app.mongodb["cars"].find(query).sort("km", -1).skip(skip).limit(RESULTS_PER_PAGE)
    results = list(cursor)  # Transformation du curseur en liste pour tests
    
    return {"results": results, "pages": pages}

@router.get("/brand/count", response_description="Count by brand")
async def brand_count(request: Request):
    query = [{"$group": {"_id": "$brand", "count": {"$sum": 1}}}]
    # Pour mongomock, aggregate renvoie directement une liste
    agg_results = request.app.mongodb["cars"].aggregate(query)
    return list(agg_results)  # Conversion en liste pour uniformité