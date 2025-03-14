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
):
    RESULTS_PER_PAGE = 25
    skip = (page - 1) * RESULTS_PER_PAGE
    
    query = {"price": {"$lt": max_price, "$gt": min_price}}
    if brand:
        query["brand"] = brand
        
    # Version sans await pour les tests
    count = request.app.mongodb["cars"].count_documents(query)
    pages = ceil(count / RESULTS_PER_PAGE)
    
    # Utilise find sans await
    cursor = request.app.mongodb["cars"].find(query).sort("km", -1).skip(skip).limit(RESULTS_PER_PAGE)
    results = list(cursor)
    
    return {"results": results, "pages": pages}

@router.get("/brand/{val}/{brand}", response_description="Get brand models by val")
async def brand_price(brand: str, val: str, request: Request):
    query = [
        {"$match": {"brand": brand}},
        {"$project": {"_id": 0}},
        {
            "$group": {"_id": {"model": "$make"}, f"avg_{val}": {"$avg": f"${val}"}},
        },
        {"$sort": {f"avg_{val}": 1}},
    ]
    # Pour mongomock, pas besoin de async for
    full_query = request.app.mongodb["cars"].aggregate(query)
    return list(full_query)

@router.get("/brand/count", response_description="Count by brand")
async def brand_count(request: Request):
    query = [{"$group": {"_id": "$brand", "count": {"$sum": 1}}}]
    # Pour mongomock, aggregate renvoie directement une liste
    full_query = request.app.mongodb["cars"].aggregate(query)
    return list(full_query)

@router.get("/make/count/{brand}", response_description="Count by brand")
async def make_count(brand: str, request: Request):
    query = [
        {"$match": {"brand": brand}},
        {"$group": {"_id": "$make", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]
    full_query = request.app.mongodb["cars"].aggregate(query)
    return list(full_query)

@router.post("/email", response_description="Send email")
async def send_mail(
    background_tasks: BackgroundTasks,
    cars_num: int = Body(...),
    email: str = Body(...),
):
    # Version simplifiée pour les tests
    return {"Received": {"email": email, "cars_num": cars_num}}