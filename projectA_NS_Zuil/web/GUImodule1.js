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
}

async function postMessage(event){

    event.preventDefault(); // Must be before first await, to prevent refresh

    message = document.getElementById("messageTxt").value;
    name = document.getElementById("nameTxt").value;
    station = document.getElementById("stationSel").value;

    has_succeeded = await eel.post_message(message, name, station)();

    document.getElementById("statusMessage").hidden = false;

    if(has_succeeded){
        document.getElementById("submitStatus").innerHTML = "Gelukt";
        clearFields();
    }
    else{
        document.getElementById("submitStatus").innerHTML = "Mislukt";
    }

    setTimeout(() => {
        document.getElementById("statusMessage").hidden = true;
    }, 1000);

}

function clearFields(){
    element = document.getElementById("messageTxt")
    element.innerHTML = ""
    element = document.getElementById("nameTxt")
    element.innerHTML = ""
}

populateStations();
document.getElementById("messageForm").addEventListener("submit", postMessage)

