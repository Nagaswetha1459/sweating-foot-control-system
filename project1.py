<!DOCTYPE html>
<html>
  <head>
    <title>sweating feet control</title>
    <style>
        body {
            background: linear-gradient(90deg, rgb(0, 143, 225), aqua, lightblue);
            margin: 0;
            padding: 0;
        }
        nav {
            background-color: black;
            overflow: hidden;
            box-shadow: 0 6px 12px white;
        }
        nav ul {
            list-style-type: none;
            display: flex;
            margin: 0;
            padding: 20px;
            text-align: center;
            justify-content: center;
        }
        nav ul li {
            padding: 0;
            font-size: 20px;
        }
        nav ul li a {
            padding: 10px;
            font-size: 25px;
            text-decoration: none;
            color: white;
            align-items: center;
            text-align: center;
        }
        pre {
            color: white;
            background-color: black;
            font-style: bold;
            text-align: center;
        }
        main {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin: 20px;
            align-items: center;
            text-align: center;
        }
        .card {
            background-color: aliceblue;
            width: 270px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px pink;
            box-sizing: 100px;
            height: 210px;
        }
        button {
            background-color: rgb(232, 146, 146);
            color: white;
            padding: 30px;
            border-radius: 100px;
            display: flex;
            box-sizing: initial;
            align-items: center;
            text-align: center;
            width: 230px;
        }
        button:hover {
            background-color: rgb(227, 158, 209);
            color: black;
        }
        .card2 {
            color: black;
            font-style: normal;
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            align-items: center;
            text-align: center;
            margin: 50px;
            height: 250px;

        }
        .dashboard {
            color: black;
            background-color: rgb(240, 240, 163);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard1{
            color: black;
            background-color: rgb(213, 163, 240);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard2 {
            color: black;
            background-color: rgb(163, 231, 240);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .dashboard3 {
            color: black;
            background-color: rgb(240, 172, 163);
            padding: 10px;
            border-radius: 5px;
            align-items: center;
            text-align: center;
            margin: 4px;
            width: 200px;
            height: 25px;
        }
        .chart-container {
            background-color: aliceblue;
            width: 570px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px pink;
            box-sizing: 100px;
            height: 350px;
        }
        canvas {
            width: 100%;
            height: 100%;
        }
    </style>
  </head>
  <body>
    <nav>
        <h1><ul><li><a href="#">Sweating Feet Control</a></li></ul></h1>
        <h3><pre>Monitor and Control Your Sweaty Feet</pre></h3>
    </nav>
    
    <main>
        <div class="card" id="liveData">
            <h3>Live Data</h3>
            <p><b>Temperature:</b> <span id="temp">25.0</span> °C</p>
            <script>
                const tempElement = document.getElementById("temp");
                function updateTemperature() {
                    tempElement.textContent = ((Math.random() * 10) + 20).toFixed(1);
                }
                setInterval(updateTemperature, 2000); // Update temperature every 2 seconds
            </script>

            <p><b>Humidity:</b> <span id="Hum">52.1%</span></p>
            <script>
                const humElement = document.getElementById("Hum");
                function updateHumidity() {
                    humElement.textContent = ((Math.random() * 10) + 50).toFixed(1) + '%';
                }
                setInterval(updateHumidity, 2000); // Update humidity every 2 seconds
            </script>

            <p><b>Heat Level:</b> <span style="color:black;">326.9 joules</span></p>
            <p><b>Cool Level:</b> <span style="color:black;">326.9 W</span></p>
        </div>

        <div class="card2" id="SensoryAlerts">
            <h3>Alerts</h3>
            <div class="dashboard">High Temperature Detected!</div>
            <div class="dashboard1">Humidity Levels are Stable</div>
            <div class="dashboard2">Heat Level is Stable</div>
            <div class="dashboard3">Cool Level is Unstable</div>
        </div>

        <div class="chart-container">
            <h1>Live Graph</h1>
            <canvas id="tempChart"></canvas>
            <script src="https://sweating-foot-control-system-3.onrender.com"></script>
            <script>
                const ctx = document.getElementById('tempChart').getContext('2d');

                const tempData = [22, 23, 24, 27, 30];

                const tempChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['1s', '2s', '3s', '4s', '5s'],
                        datasets: [{
                            label: 'Temperature (°C)',
                            data: tempData,
                            borderColor: '#4caf50', // Green
                            fill: true,
                            backgroundColor: 'rgba(76, 175, 80, 0.2)',
                        }]
                    }
                });

                function updateGraph() {
                    const temp = Math.random() * 10 + 22; // Generate random temperature
                    tempData.push(temp);
                    tempData.shift(); // Remove the oldest data point
                    tempChart.update();
                }

                setInterval(updateGraph, 5000); // Update graph every 5 seconds
            </script>
        </div>
    </main>
  </body>
</html>
