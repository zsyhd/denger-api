#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify

app = Flask(__name__)
port = 3000

# داده‌های چاه خطرناک
danger_well = {
    "WellId": 2,
    "WellName": "Well 2",
    "Status": "Danger",   # وضعیت
    "Color": "#C70039"    # قرمز برای خطر
}

# API برای danger well
@app.route("/api/danger", methods=["GET"])
def get_danger_well():
    return jsonify(danger_well)

if __name__ == "__main__":
    print(f"API running at http://localhost:{port}")
    app.run(port=port)

from fastapi import FastAPI 
 
app = FastAPI(title=" Denger API") 
 
@app.get("/") 
def root(): 
    return { 
        "message": "⚡  Denger API is running!", 
        "docs": "/docs", 
        "example": "/denger/test" 
    } 
 
@app.get("/denger/test") 
def test(): 
    return {"status": "ok", "note": "API working successfully 💚"} 