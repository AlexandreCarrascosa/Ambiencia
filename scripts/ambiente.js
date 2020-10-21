var myTab = document.getElementById('myTable');

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
