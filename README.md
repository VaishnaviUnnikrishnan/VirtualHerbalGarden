# 🌿 Virtual Herbal Garden

**Virtual Herbal Garden** is an interactive web-based platform designed to explore and learn about medicinal plants through **3D models** and **data analytics**. It combines **FastAPI**, **MongoDB**, and **Three.js** to provide a **dynamic visualization** and **scientific insights** into various herbs and their ecological impact.

---

## 📌 Features
✅ **Explore 3D Plant Models**: View high-quality, interactive 3D models of medicinal plants.  
✅ **Dynamic Database**: Fetch herbal plant details from **MongoDB** dynamically.  
✅ **Scientific Insights**: See oxygen emission, CO₂ reduction, medicinal properties, and more.  
✅ **Interactive Map**: Visualize plant growth regions on a world map using **Folium**.  
✅ **REST API Support**: Fetch plant data programmatically.  

---

## 📂 Project Structure

```
VirtualPlantBot/
│── app/
│   ├── models/               # 3D GLB models of plants
│   │   ├── Aloe Vera.glb
│   │   ├── Banana.glb
│   │   ├── Chamomile.glb
│   │   ├── ...
│   ├── templates/            # HTML templates
│   │   ├── home.html         # Homepage
│   │   ├── impact.html       # Impact analysis page
│   │   ├── plant_viewer.html # 3D plant viewer
│── venv/                     # Virtual environment
│── main.py                   # FastAPI server
│── requirements.txt           # Project dependencies
│── README.md                 # Documentation
```

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VaishnaviUnnikrishnan/VirtualHerbalGarden
cd VirtualPlantBot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start MongoDB Server  
Ensure MongoDB is running locally:
```bash
mongod --dbpath /path/to/mongodb/data
```

### 5️⃣ Run the FastAPI Server
```bash
uvicorn main:app --reload
```

---

## 🔗 API Endpoints

| Method | Endpoint               | Description                                  |
|--------|------------------------|----------------------------------------------|
| GET    | `/`                    | Homepage showing available plant models     |
| GET    | `/view/{plant_name}`    | View 3D model of a selected plant           |
| GET    | `/impact/{plant_name}`  | View environmental impact details of plant  |
| GET    | `/api/plant/{plant_name}` | Fetch plant details from MongoDB as JSON |

---

## 🌍 Interactive Map  
The **Impact Dashboard** dynamically generates a **Folium map** showing plant growth regions. If a plant has known coordinates, markers will be displayed for each location.

---

## 📜 Example MongoDB Schema  
Your MongoDB collection **herbal_plants** should follow this schema:

```json
{
  "name": "Aloe Vera",
  "botanical_name": "Aloe barbadensis miller",
  "origin_place": "Arabian Peninsula",
  "origin_year": "Ancient",
  "herbal_values": ["Anti-inflammatory", "Skin healing"],
  "oxygen_emitted_per_year": 12.5,
  "co2_reduction_per_year": 8.7,
  "water_purification_rate": 4.3,
  "medicinal_uses_count": 15,
  "diseases_cured_or_relieved": ["Skin burns", "Diabetes"],
  "antioxidant_level": 9.5,
  "growth_rate_per_month": 2.1,
  "growth_regions": ["India", "China", "Mexico"],
  "growth_coords": [{"lat": 28.7041, "lon": 77.1025, "region": "India"}]
}
```

---

## 🛠 Technologies Used
- **Backend**: FastAPI 🚀  
- **Database**: MongoDB 🍃  
- **Frontend**: HTML, CSS, Bootstrap 🎨  
- **3D Rendering**: Three.js 🌐  
- **Mapping**: Folium 🗺  

---

## 📜 License
This project is licensed under the **MIT License**.

---
![image](https://github.com/user-attachments/assets/08cd9f82-cb48-43b7-8900-acff1f034bb4)

![image](https://github.com/user-attachments/assets/d08920c0-4a79-4697-a07e-7a0cf9312c85)

![image](https://github.com/user-attachments/assets/6b7d0c61-d20a-4298-98e0-227349a6324e)





