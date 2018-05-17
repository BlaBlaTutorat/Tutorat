// Fonction executée lors de la pression d'une touche clavier
$(document).keydown(function (event) {
    if (event.keyCode === 123) { // Prevent F12
        return false;
    } else if (event.ctrlKey && event.shiftKey && event.keyCode === 73) { // Prevent Ctrl+Shift+I
        return false;
    }
});

// Fonction qui désactive le menu affiché lors du clique droit
$(document).on("contextmenu", function (e) {
    e.preventDefault();
});

// Fonction pour ouvrir page de profil
function open_profile_page(mail) {
    window.open('/profile/view/' + mail, 'profil', 'height=625,width=700');
}

function setCharAt(str,index,chr) {
    if(index > str.length-1) return str;
    return str.substr(0,index) + chr + str.substr(index+1);
}

function horaire_click(event, id, class_name) {
    var data = document.getElementById('horaires_data').value;
    var day = parseInt(id.split(" ")[0]);
    var hour = parseInt(id.split(" ")[1]);
    var index = (day*22)+hour;

    if (class_name === "red") {
        document.getElementById(id).classList.remove("red");
        document.getElementById(id).classList.add("white");
        data = setCharAt(data, index, "0")
    } else {
        document.getElementById(id).classList.remove("white");
        document.getElementById(id).classList.add("red");
        data = setCharAt(data, index, "1")
    }

    document.getElementById('horaires_data').value = data;
}