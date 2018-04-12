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
function open_profile_page(mail){
    window.open('/profile/view/' + mail,'profil','height=625,width=700')
}