from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
import os
import folium
import json

app = FastAPI()

# Mount static directories
app.mount("/models", StaticFiles(directory="app/models"), name="models")


# Jinja2 Templates
templates = Jinja2Templates(directory="templates")

# MongoDB Connection
client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["HerbalGardenDB"]
collection = db["herbal_plants"]


@app.get("/")
async def home(request: Request):
    """Serve the homepage with available plant models"""
    models_path = "app/models"
    plant_models = [f for f in os.listdir(models_path) if f.endswith(".glb")]
    return templates.TemplateResponse("home.html", {"request": request, "plant_models": plant_models})


@app.get("/view/{plant_name}")
async def view_plant(request: Request, plant_name: str):
    """Serve the 3D viewer page with the selected model"""
    return templates.TemplateResponse("plant_viewer.html", {"request": request, "plant_name": plant_name})


@app.get("/impact/{plant_name}")
async def plant_impact(request: Request, plant_name: str):
    """Serve the impact dashboard page"""
    plant = await collection.find_one({"name": plant_name.replace('.glb', '')})

    if not plant:
        return JSONResponse({"error": "Plant not found"}, status_code=404)

    # Map the database fields to our expected structure
    plant_data = {
        "name": plant.get("name", "Unknown"),
        "botanical_name": plant.get("botanical_name", "Unknown"),
        "origin_place": plant.get("origin_place", "Unknown"),
        "origin_year": plant.get("origin_year", "Unknown"),
        "herbal_values": plant.get("herbal_values", []),
        "oxygen_emitted_per_year": plant.get("oxygen_emitted_per_year", 0),
        "co2_reduction_per_year": plant.get("co2_reduction_per_year", 0),
        "water_purification_rate": plant.get("water_purification_rate", 0),
        "medicinal_uses_count": plant.get("medicinal_uses_count", 0),
        "diseases_cured_or_relieved": plant.get("diseases_cured_or_relieved", 0),
        "antioxidant_level": plant.get("antioxidant_level", 0),
        "growth_rate_per_month": plant.get("growth_rate_per_month", 0),
        "growth_regions": plant.get("growth_regions", []),
        "growth_coords": plant.get("growth_coords", [])
    }

    # Generate folium map if coordinates exist
    map_html = "<div class='alert alert-warning'>Location data not available</div>"
    if plant_data["growth_coords"] and len(plant_data["growth_coords"]) > 0:
        try:
            # Use the first coordinate as the map center
            first_coord = plant_data["growth_coords"][0]
            m = folium.Map(location=[first_coord["lat"], first_coord["lon"]], zoom_start=2)

            # Add markers for all growth regions
            for coord in plant_data["growth_coords"]:
                folium.Marker(
                    [coord["lat"], coord["lon"]],
                    popup=coord["region"]
                ).add_to(m)

            map_html = m._repr_html_()
        except Exception as e:
            print(f"Error generating map: {e}")
            map_html = "<div class='alert alert-danger'>Error displaying map data</div>"

    return templates.TemplateResponse("impact.html", {
        "request": request,
        "plant_name": plant_name,
        "plant_data": plant_data,
        "map_html": map_html,
        "herbal_values_json": json.dumps(plant_data["herbal_values"])
    })

@app.get("/api/plant/{plant_name}")
async def get_plant_details(plant_name: str):
    """Fetch plant details from MongoDB"""
    plant = await collection.find_one({"name": plant_name.replace('.glb', '')})

    if plant:
        return JSONResponse({
            "name": plant.get("name", "Unknown"),
            "botanical_name": plant.get("botanical_name", "Unknown"),
            "origin_place": plant.get("origin_place", "Unknown"),
            "origin_year": plant.get("origin_year", "Unknown"),

        })
    return JSONResponse({"error": "Plant not found"}, status_code=404)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)