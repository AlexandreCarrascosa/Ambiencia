var pvs = document.getElementById("pvs")
var ppv = document.getElementById("ppv")
var rms = document.getElementById("rms")
var rm = document.getElementById("rm")
var tpo = document.getElementById("tpo")
var v = document.getElementById("v")
var p = document.getElementById("p")
var h = document.getElementById("h")
var tbu = document.getElementById("tbu")

xmlhttp = new XMLHttpRequest();
xmlhttp.open("GET", "../calc.xml", false);
xmlhttp.send();
xmlDoc = xmlhttp.responseXML;

var x = xmlDoc.getElementsByTagName("root");

for (i=0;i<x.length;i++)
    {
        pvs.innerHTML = x[i].getElementsByTagName("PVS")[0].childNodes[0].nodeValue;
        document.write("<tr><td>");
        document.write("</td><td>");
        ppv.innerHTML = x[i].getElementsByTagName("PPV")[0].childNodes[0].nodeValue;
        document.write("</td><td>");
        rms.innerHTML = x[i].getElementsByTagName("RMS")[0].childNodes[0].nodeValue;
        document.write("</td><td>");
        rm.innerHTML =(x[i].getElementsByTagName("RM")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        tpo.innerHTML =(x[i].getElementsByTagName("TPO")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        v.innerHTML =(x[i].getElementsByTagName("v")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        p.innerHTML =(x[i].getElementsByTagName("p")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        h.innerHTML =(x[i].getElementsByTagName("h")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        tbu.innerHTML =(x[i].getElementsByTagName("TBU")[0].childNodes[0].nodeValue);
        document.write("</td></tr>");
    }
document.write('</table></div></div></section>');
