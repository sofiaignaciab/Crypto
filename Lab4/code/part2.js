// ==UserScript==
// @name         Obtener Contraseña de Cripto y Contar Mensajes Cifrados
// @namespace    http://tampermonkey.net/
// @version      0.4
// @description  Obtener la llave y mensajes
// @author       Tu Nombre
// @match        https://cripto.tiiny.site/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function getUppercase(text) {
        return text.match(/[A-Z]/g).join('');
    }

    let text = document.body.innerText;
    let key = getUppercase(text);
    let hash = CryptoJS.SHA256(key).toString();

    console.log("La contraseña es: " + key);
    console.log("Hash de la contraseña es: " + hash);

    let divs = document.querySelectorAll('div[class^="M"]');
    let cant = divs.length;

    console.log("Los mensajes cifrados son: " + cant);
})();