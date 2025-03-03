let punts = 0;               
let encertsSeguits = 0;     
let totalPartides = 0;       
let partidesGuanyades = 0;    

const paraula = document.getElementById("palabraJugador");
const botoIniciar = document.getElementById("comenzarJuego");

function iniciarPartida() {
    const valorParaula = paraula.value;

    document.getElementById("body").style.backgroundColor = "white";
    if (/\d/.test(valorParaula)) {
        alert("La paraula no pot contenir números.");
    } else if (valorParaula.length < 4) {
        alert("La paraula ha de tenir almenys 4 lletres.");
    } else {
        punts = 0;
        encertsSeguits = 0;

        configurarParaula();
        paraula.disabled = true;
        botoIniciar.disabled = true;
    }
}

function canviaTipus() {
    paraula.type = paraula.type === "password" ? "text" : "password";
}

function configurarParaula() {
    let paraulaEndevinar = document.getElementById("palabraSecreta");
    let textParaula = paraula.value;
    let guions = "_".repeat(textParaula.length);

    paraulaEndevinar.textContent = guions;

    paraulaEndevinar.style.letterSpacing = "10px";
}

function verificarLletra(boto) {
    const lletraSeleccionada = boto.textContent.toUpperCase();
    boto.disabled = true;
    const paraulaSecreta = paraula.value.toUpperCase();
    const paraulaEndevinar = document.getElementById("palabraSecreta");
    let estatActual = paraulaEndevinar.textContent.split("");

    let trobada = false;
    let ocurrencies = 0;

    for (let i = 0; i < paraulaSecreta.length; i++) {
        if (paraulaSecreta[i] === lletraSeleccionada) {
            estatActual[i] = lletraSeleccionada;
            trobada = true;
            ocurrencies++;
        }
    }
    paraulaEndevinar.textContent = estatActual.join("");
    if (trobada) {
        encertsSeguits++;
        punts += encertsSeguits * ocurrencies;
    } else {
        encertsSeguits = 0;
        punts = Math.max(0, punts - 1);
    }
    document.getElementById("puntos").textContent = punts;

    if (!estatActual.includes("_")) {
        totalPartides++;
        partidesGuanyades++;
        acabarPartida();
    }
}
// acabar la partida
function acabarPartida() {
    paraula.disabled = false;
    botoIniciar.disabled = false;
    const percentatgeGuanyades = ((partidesGuanyades / totalPartides) * 100).toFixed(2);
    document.getElementById("body").style.backgroundColor = "green";
    document.getElementById("totalPartidas").textContent = totalPartides;
    document.getElementById("partidasGanadas").textContent = partidesGuanyades;
    document.getElementById("porcentajeVictorias").textContent = percentatgeGuanyades + "%";

    alert(`Felicitats! Has endevinat la paraula. Punts: ${punts}`);
}
