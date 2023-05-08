
console.log("hola mundo");
function bloquearArea(texto){

const habilirarServicio = document.getElementById("servicio")
const desahabilitarArea = document.getElementById("area");
habilirarServicio.disabled = false;
desahabilitarArea.disabled = true;

console.log(texto);

const area = document.getElementById("selecionArea");
area.innerHTML= texto;



};

function bloquearServicio(texto){
    const habilitarDoctor = document.getElementById("doctor");
    const desahabilitarServicio= document.getElementById("servicio");
    habilitarDoctor.disabled = false;
    desahabilitarServicio.disabled = true;

    const servicio = document.getElementById("selecionServicio");
    servicio.innerHTML=texto;
 

};

function bloquearMedico(texto){
    const desahabilitarDoctor= document.getElementById("doctor");
    desahabilitarDoctor.disabled = true;

    const doctor = document.getElementById("selecionDoctor");
    doctor.innerHTML=texto;
    desahabilitarDoctor.className="accordion-button collapsed";
    desahabilitarDoctor.dataset.araExpanded="false";
    var cerrar = document.getElementById("flush-collapseThree");
    cerrar.className="accordion-collapse collapse";
    desahabilitarDoctor.disabled = true;

};