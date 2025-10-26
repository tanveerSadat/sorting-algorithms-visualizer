function getBubbleSort() {

    const input = document.getElementById("bubblesortinput").value;

    const url = "/bubblesort"

    arr = input.replace(/^\[|\]$/g, '').split(",")
                    .map(item => item.trim())
                    .map(Number)
                    .filter(num => !isNaN(num));

    console.log(arr)

    $.ajax({
        url: '/bubblesort',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ arr: arr }),
        success: function(data) {
            console.log(data);
            updateBubbleSortSolution(data)
        }
    });
}

function updateBubbleSortSolution(data){
    // Array, i, j, swappedBool

    //clear the div
    var solutionDiv = document.getElementById("bubblesortsolution");
    solutionDiv.innerHTML = "";

    var length = data.length
    var table = document.createElement("solutionTable");
    table.style.borderCollapse = "collapse";

    for(var i = 0; i < length; i++){

        var arr = data[i][0];
        var iIndex = data[i][1];
        var jIndex = data[i][2];
        var swapped = data[i][3];

        // Row 1: array values
        var row1 = document.createElement("tr");
        arr.forEach(num => {
            var cell = document.createElement("td");
            cell.textContent = num;
            cell.style.border = "1px solid black";
            cell.style.padding = "5px";
            cell.style.textAlign = "center";
            cell.style.backgroundColor  = "#000000ff"
            row1.appendChild(cell);
        });
        table.appendChild(row1);
        
        var row2 = document.createElement("tr");
        arr.forEach((_, index) => {
            var cell = document.createElement("td");
            cell.style.border = "1px solid black";
            cell.style.padding = "5px";
            cell.style.textAlign = "center";
            cell.style.backgroundColor  = "#000000ff"

            if (index === iIndex && index === jIndex) {
                cell.textContent = "i,j";
            } else if (index === iIndex) {
                cell.textContent = "i";
            } else if (index === jIndex) {
                cell.textContent = "j";
                cell.style.backgroundColor = swapped ? "#5e905eff" : "#000000ff";
            } else if (index === jIndex + 1) {
                cell.textContent = "j + 1";
                cell.style.backgroundColor = swapped ? "#5e905eff" : "#000000ff";
            } else {
                cell.textContent = "";
            }
            
            row2.appendChild(cell);
        });
        table.appendChild(row2);

        var row3 = document.createElement("tr");
        arr.forEach(() => {
            var cell = document.createElement("td");
            cell.textContent = "";
            cell.style.padding = "12px";
            row3.appendChild(cell);
        });
        table.appendChild(row3);
    }
    
    solutionDiv.appendChild(table);
}

function getSelectionSort() {

    const input = document.getElementById("selectionsortinput").value;

    const url = "/selectionsort"

    arr = input.replace(/^\[|\]$/g, '').split(",")
                    .map(item => item.trim())
                    .map(Number)
                    .filter(num => !isNaN(num));

    console.log(arr)

    $.ajax({
        url: '/selectionsort',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ arr: arr }),
        success: function(data) {
            console.log(data);
            updateSelectionSortSolution(data)
        }
    });
}

function updateSelectionSortSolution(data){
    // Array, i, j, m, swappedBool

    //clear the div
    var solutionDiv = document.getElementById("selectionsortsolution");
    solutionDiv.innerHTML = "";

    var length = data.length
    var table = document.createElement("solutionTable");
    table.style.borderCollapse = "collapse";

    for(var i = 0; i < length; i++){

        var arr = data[i][0];
        var iIndex = data[i][1];
        var jIndex = data[i][2];
        var mIndex = data[i][3];
        var swapped = data[i][4];

        // Row 1: array values
        var row1 = document.createElement("tr");
        arr.forEach(num => {
            var cell = document.createElement("td");
            cell.textContent = num;
            cell.style.border = "1px solid black";
            cell.style.padding = "5px";
            cell.style.textAlign = "center";
            cell.style.backgroundColor  = "#000000ff"
            row1.appendChild(cell);
        });
        table.appendChild(row1);
        
        var row2 = document.createElement("tr");
        arr.forEach((_, index) => {
            var cell = document.createElement("td");
            cell.style.border = "1px solid black";
            cell.style.padding = "5px";
            cell.style.textAlign = "center";
            cell.style.backgroundColor  = "#000000ff"

            if (index === iIndex && index === jIndex) {
                cell.textContent = "i,j";
                cell.style.backgroundColor = swapped ? "#5e905eff" : "#000000ff";
            } else if (index === iIndex) {
                cell.textContent = "i";
                cell.style.backgroundColor = swapped ? "#5e905eff" : "#000000ff";
            } else if (index === jIndex) {
                cell.textContent = "j";
            } else {
                cell.textContent = "";
            }
            
            row2.appendChild(cell);
        });
        table.appendChild(row2);

        var row3 = document.createElement("tr");
        arr.forEach((_, index) => {
            var cell = document.createElement("td");
            cell.style.border = "1px solid black";
            cell.style.padding = "12px";
            cell.style.textAlign = "center";
            cell.style.backgroundColor  = "#000000ff"

            if (index === mIndex) {
                cell.textContent = "m";
                cell.style.backgroundColor = swapped ? "#5e905eff" : "#000000ff";
            }

            row3.appendChild(cell);
        });
        table.appendChild(row3);

        var row4 = document.createElement("tr");
        arr.forEach(() => {
            var cell = document.createElement("td");
            cell.textContent = "";
            cell.style.padding = "12px";
            row4.appendChild(cell);
        });
        table.appendChild(row4);
    }
    
    solutionDiv.appendChild(table);
}