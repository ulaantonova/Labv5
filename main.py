
from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI(title="Ship Navigation API")

@app.get("/calculate")
async def calculate(
    distance: float = Query(..., description="Відстань до порту в морських милях"),
    mode: str = Query("standard", description="Режим ходу: standard або eco")
):
    """
    Ендпоінт для розрахунку параметрів руху судна.
    """
    ship_name = "AutoShip-01"
    
    
    if mode.lower() == 'eco':
        speed = 12.0  # обмеження швидкості
        fuel_consumption = 0.5  # умовні одиниці на милю
    else:
        speed = 20.0  # стандартна швидкість
        fuel_consumption = 0.9
        mode = "standard"

    # Обчислення
    travel_time = round(distance / speed, 2)
    total_fuel = round(distance * fuel_consumption, 2)

    return {
        "ship_name": ship_name,
        "mode": mode.upper(),
        "input_distance_nm": distance,
        "calculated_speed_knots": speed,
        "estimated_time_hours": travel_time,
        "estimated_fuel_needed": total_fuel,
        "timestamp": datetime.now().strftime('%H:%M:%S')
    }

if __name__ == "__main__":
    import uvicorn
   
    uvicorn.run(app, host="127.0.0.1", port=5000)