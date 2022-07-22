function hideField() {
    var returnfield = document.getElementById("select").value;
    if (returnfield == "") {
        document.getElementById("returned").style.display = "none";
    }
    else if (returnfield == "borrow") {
        document.getElementById("returned").style.display = "none";
    }
}
function showField() {
    var returnfield = document.getElementById("select").value;
    if (returnfield == "return") {
        document.getElementById("returned").style.display = "block";
    }
}