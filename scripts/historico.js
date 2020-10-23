xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET","../data.xml",false);
xmlhttp.send();
xmlDoc=xmlhttp.responseXML;

document.write("<section class='buttons'><div class='buttom'><div class='graph'>")
document.write("<table class='history' id='myTable'>")
document.write("<tr><th><img src='../icons/datetime.svg'/> Data/Hora</th>")
document.write('<th><img src="../icons/temp.svg" /> Temperatura (ºC)</th>')
document.write('<th><img src="../icons/moisture.svg" /> Umidade (%)</th>')
document.write('<th><img src="../icons/waterdrop.svg"/> Irrigação</th>')
document.write('<th><img src="../icons/fan.svg"/> Ventilação</th>')
document.write('<th><img src="../icons/lamp.svg"/> Iluminação</th></tr>')

var x = xmlDoc.getElementsByTagName("Info");

for (i=0;i<x.length;i++)
    {
        document.write("<tr><td>");
        document.write(x[i].getElementsByTagName("data")[0].childNodes[0].nodeValue);
        document.write(", ")
        document.write(x[i].getElementsByTagName("hora")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        document.write(x[i].getElementsByTagName("temp")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        document.write(x[i].getElementsByTagName("umd")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        document.write(x[i].getElementsByTagName("aspr")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        document.write(x[i].getElementsByTagName("vent")[0].childNodes[0].nodeValue);
        document.write("</td><td>");
        document.write(x[i].getElementsByTagName("lamp")[0].childNodes[0].nodeValue);
        document.write("</td></tr>");
    }
document.write('</table></div></div></section>')

var myTab = document.getElementById('myTableAtual');

for (i = 1; i < myTab.rows.length; i++) {

    // GET THE CELLS COLLECTION OF THE CURRENT ROW.
    var objCells = myTab.rows.item(i).cells;

    // LOOP THROUGH EACH CELL OF THE CURENT ROW TO READ CELL VALUES.
    for (var j = 0; j < objCells.length; j++) {
        
        if(objCells.item(j).innerHTML == "OFF"){
            objCells.item(j).style.color = "red"
        }

        if(objCells.item(j).innerHTML == "ON"){
            objCells.item(j).style.color = 'lightgreen'
        }
    }

}