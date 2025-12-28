from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Define a Pydantic model for data validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    is_offer: bool = False # Field with a default value

# 2. Create a FastAPI instance
app = FastAPI()

# 3. Define a POST endpoint that uses the Pydantic model
@app.post("/items/")
def create_item(item: Item):
    # The 'item' parameter is an instance of the Item model
    # FastAPI automatically parses and validates the incoming JSON data against this model
    
    # You can access model attributes directly
    item_dict = item.model_dump() # use model_dump() for Pydantic v2+
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    
    return {"message": "Item created successfully", "item": item_dict}

# You can also use Pydantic models for response validation
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # In a real application, you would fetch data from a database
    # For this example, we return a mock Item
    return {
        "name": "Sample Item",
        "price": 19.99,
        "is_offer": True
    }
