// ==UserScript==
// @name         Obtener contraseña
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  Obtener la llave
// @author       you
// @match        https://cripto.tiiny.site/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function obtenerMayusculas(texto) {
        return texto.match(/[A-Z]/g).join('');
    }

    let textoCompleto = document.body.innerText;
    let contrasena = obtenerMayusculas(textoCompleto);
    let hash = CryptoJS.SHA256(contrasena).toString();

    console.log("La contraseña es: " + contrasena);
    console.log("Hash de la contraseña es: " + hash);
})();