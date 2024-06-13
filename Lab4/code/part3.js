// ==UserScript==
// @name         Obtener Contraseña de Cripto y Contar Mensajes Cifrados
// @namespace    http://tampermonkey.net/
// @version      0.4
// @description  Obtener llave y mensajes
// @author       Sofia
// @match        https://cripto.tiiny.site/
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function getUppercase(text) {
        return text.match(/[A-Z]/g).join('');
    }

    function decrypt3DES(ciphertext, key) {
        let bytes = CryptoJS.TripleDES.decrypt(ciphertext, CryptoJS.enc.Utf8.parse(key), {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
        return bytes.toString(CryptoJS.enc.Utf8);
    }

    let text = document.body.innerText;
    let key = getUppercase(text);
    let hash = CryptoJS.SHA256(key).toString();

    console.log("La contraseña es: " + key);
    console.log("Hash de la contraseña es: " + hash);

    let divs = document.querySelectorAll('div[class^="M"]');
    let cant = divs.length;

    console.log("Los mensajes cifrados son: " + cant);

    for (let i = 0; i < cant; i++) {
        let ciphertext = divs[i].id;
        let plaintext = decrypt3DES(ciphertext, key);

        console.log(ciphertext + " " + plaintext);

        let p = document.createElement('p');
        p.innerText = plaintext;
        document.body.appendChild(p);
    }

})();
