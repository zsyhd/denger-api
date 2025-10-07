from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Zahra's Denger API")

# داده‌ی چاه خطرناک
danger_well = {
    "WellId": 2,
    "WellName": "Well 2",
    "Status": "Danger",
    "Color": "#C70039"   # قرمز برای وضعیت خطر
}

@app.get("/")
def home():
    return {
        "message": "⚡ Zahra's Denger API is running successfully!",
        "docs": "/docs",
        "example_routes": ["/api/danger", "/denger/test"]
    }

@app.get("/api/danger")
def get_danger_well():
    return JSONResponse(content=danger_well)

@app.get("/denger/test")
def test():
    return {"status": "ok", "note": "API working successfully 💚"}
