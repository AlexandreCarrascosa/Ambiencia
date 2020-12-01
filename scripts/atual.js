var data = new Date();
var hora = data.getHours() + ":" + data.getMinutes();
var dia = data.getDate() + "/" + data.getMonth() + "/" + data.getFullYear();

var local = document.getElementById("titleAtual")
var hora = document.getElementById("horas")
var temp = document.getElementById("temperatura")
var umid = document.getElementById("umidade")
var irri = document.getElementById("irrigacao")
var vent = document.getElementById("ventilador")
var lamp = document.getElementById("lampadas")

xmlhttp= new XMLHttpRequest();
xmlhttp.open("GET","..//atual.xml",false);
xmlhttp.send();
xmlDoc=xmlhttp.responseXML;

var x = xmlDoc.getElementsByTagName("Info");



for (i=0;i<x.length;i++)
    {
        local.innerHTML = x[i].getElementsByTagName("data")[0].childNodes[0].nodeValue;
        document.write("<tr><td>");
        document.write("</td><td>");
        hora.innerHTML = x[i].getElementsByTagName("hora")[0].childNodes[0].nodeValue;
        document.write("</td><td>");
        temp.innerHTML = x[i].getElementsByTagName("temp")[0].childNodes[0].nodeValue;
        document.write("</td><td>");
        umid.innerHTML =(x[i].getElementsByTagName("umd")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        irri.innerHTML =(x[i].getElementsByTagName("aspr")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        vent.innerHTML =(x[i].getElementsByTagName("vent")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        lamp.innerHTML =(x[i].getElementsByTagName("lamp")[0].childNodes[0].nodeValue);
        document.write("</td></tr>");
    }
document.write('</table></div></div></section>');


if (irri.innerHTML == "OFF"){
    irri.style.color = 'red'
} else {
    irri.style.color = 'lightgreen'
}

if (vent.innerHTML == "OFF"){
    vent.style.color = 'red'
} else {
    vent.style.color = 'lightgreen'
}

if (lamp.innerHTML == "OFF"){
    lamp.style.color = 'red'
} else {
    lamp.style.color = 'lightgreen'
}