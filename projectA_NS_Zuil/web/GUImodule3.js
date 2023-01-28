async function populateStations(){
    var stations = await eel.get_stations()();
    var stationsSelect = document.getElementById('stationSel');

    for(station of stations)
    {
       var opt = document.createElement("option");
       opt.value = station;
       opt.innerHTML = station;
       stationsSelect.appendChild(opt);
    }

    updateWeather();
}

async function populateMessages(){
    var messages = await eel.get_messages()();
    var messageTable = document.getElementById('messagesTable');

    for(message of messages)
    {
        var row = messageTable.insertRow(-1);
        for (let c = 0; c < message.length; c++) {
            var cell = row.insertCell(c);
            cell.innerHTML = message[c];
         }
    }
}

async function updateWeather() {
    var city = document.getElementById("stationSel").value;
    var weatherStatus = await eel.get_weather(city)();
    var weatherSpan = document.getElementById('weatherSpan');
    weatherSpan.innerHTML = weatherStatus;
}

populateStations();
populateMessages();
document.getElementById("stationSel").addEventListener("change", updateWeather);
