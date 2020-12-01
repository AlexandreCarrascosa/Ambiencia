xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET","../data.xml",false);
xmlhttp.send();
xmlDoc=xmlhttp.responseXML;

var x = xmlDoc.getElementsByTagName("Info");
const y = [];
var label = 'Info';

for (i=0;i<x.length;i++)
    {
      
      var obj = {
        "data": x[i].getElementsByTagName("data")[0].childNodes[0].nodeValue,
        "hora": x[i].getElementsByTagName("hora")[0].childNodes[0].nodeValue,
        "temp": x[i].getElementsByTagName("temp")[0].childNodes[0].nodeValue,
        "umd":  x[i].getElementsByTagName("umd")[0].childNodes[0].nodeValue,
        "aspr": x[i].getElementsByTagName("aspr")[0].childNodes[0].nodeValue,
        "vent": x[i].getElementsByTagName("vent")[0].childNodes[0].nodeValue,
        "lamp": x[i].getElementsByTagName("lamp")[0].childNodes[0].nodeValue,
      }
      
      y.push(obj)
    }

//const data = y
console.log(y)

const data = y.map(item => {return [`${item.data +'||'+ item.hora} ${item.temp} ${item.umd} ${item.aspr} ${item.vent} ${item.lamp}  `]})

//const data = Array.from({length: 100})
//.map((_, i) => `Item ${(i + 1)}`)


console.log(data)
//===============================

let perPage = 24
const state = {
    page: 1,
    perPage,
    totalPage: Math.ceil(data.length / perPage),
    maxVisibleButtons: 2
}

const html = {
    get(element){
        return document.querySelector(element)
    }
}


const controls = {
    next () {
        state.page++
        
        const lastPage = state.page > state.totalPage
        if (lastPage) {
            state.page--
        }
    },
    prev () {
        state.page--

        if(state.page < 1){
            state.page++
        }
    },
    goTo (page) {
        if (page < 1){
            page = 1
        }

        state.page = +page

        if (page > state.totalPage){
            state.page = state.totalPage
        }
    },
    createListeners(){
        html.get('.first').addEventListener('click', () => {
            controls.goTo(1)
            update()
        })

        html.get('.last').addEventListener('click', () => {
            controls.goTo(state.totalPage)
            update()
        })

        html.get('.next').addEventListener('click', () => {
            controls.next()
            update()
        })

        html.get('.prev').addEventListener('click', () => {
            controls.prev()
            update()
        })
    } 
    
}


const list = {
    create(item){
        const div = document.createElement('div')
        div.classList.add('item')
        div.innerHTML = item


        html.get('.list').appendChild(div)
    },
    
    update(){
        html.get('.list').innerHTML = ""

        let page = state.page - 1
        let start = page * state.perPage
        let end = start + state.perPage

        const paginatedItems = data.slice(start, end)
        
        paginatedItems.forEach(list.create)
    }    
}

const buttons = {
    element: html.get('#paginate .numbers'),

    create(number){
        const button = document.createElement('div')
        button.innerHTML = number;

        if(state.page == number) {
            button.classList.add('active')
        }

        button.addEventListener('click', (event) => {
            const page = event.target.innerText

            controls.goTo(page)
            update() 
        })

        buttons.element.appendChild(button)

    },
    update(){
        buttons.element.innerHTML = ""
        const {maxLeft, maxRight} = buttons.calculateMaxVisible()
        console.log(maxLeft, maxRight)

        for(let page = maxLeft; page <= maxRight; page ++ ){
            buttons.create(page)
        }
    },
    calculateMaxVisible(){
        const {maxVisibleButtons} = state
        
        let maxLeft = state.page - Math.floor(maxVisibleButtons / 2)
        let maxRight = state.page + Math.floor(maxVisibleButtons / 2)

        if (maxLeft < 1){
            maxLeft = 1
            maxRight = maxVisibleButtons        
        }

        if (maxRight > state.totalPage){
            maxLeft = state.totalPage - (maxVisibleButtons - 1)
            maxRight = state.totalPage

            if (maxLeft < 1) {maxLeft = 1}
        }

        

        return {maxLeft, maxRight}

    }
}


function update(){
    list.update()
    buttons.update()
}

function init() {
    update()
    controls.createListeners()
    
}

init()

