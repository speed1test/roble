//rendreizar el grafico
const renderizarPruebas =(data,labels)=>{
    
    var ctx = document.getElementById('pruebas_grafico').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas',
                data: data,
                //aqui pueden editar los colores
                backgroundColor: [
                    'rgba(33, 36, 89, 0.7)',
                    'rgba(2, 100, 140, 0.7)',
                    'rgba(2, 140, 140, 0.7)',
                    'rgba(4, 191, 172, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(33, 36, 89, 1)',
                    'rgba(2, 100, 140, 1)',
                    'rgba(2, 140, 140, 1)',
                    'rgba(4, 191, 172, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],



                borderWidth: 1
            }]
        },
        options: {
           
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
           
        }
    });
}

//pero antes obtengo los datos del urrl.py
const getdataPruebas =()=>{
   
    fetch('/pruebas_resumen')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const pruebas_resumen_d =results.pruebas_resumen;
        const [labels,data]=[
            Object.keys(pruebas_resumen_d),
            Object.values(pruebas_resumen_d),
        ];
        //renderizo el grafico
        renderizarPruebas(data,labels);
    });
};

//mismo proceso con este otro grafico
const renderizarPruebasPosi =(data,labels)=>{
    
    var ctx = document.getElementById('pruebas_positivas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas',
                data: data,
                backgroundColor: [
                    'rgba(33, 36, 89, 0.7)',
                    'rgba(2, 100, 140, 0.7)',
                    'rgba(2, 140, 140, 0.7)',
                    'rgba(4, 191, 172, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(33, 36, 89, 1)',
                    'rgba(2, 100, 140, 1)',
                    'rgba(2, 140, 140, 1)',
                    'rgba(4, 191, 172, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],



                borderWidth: 1
            }]
        },
        options: {
           
            legend: {
                display: true
            },
            
           
        }
    });
}


const getdataPruebasPosi =()=>{
   
    fetch('/pruebas_resumen_genero')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const pruebas_resumen_d =results.pruebas_resumen_genero;
        const [labels,data]=[
            Object.keys(pruebas_resumen_d),
            Object.values(pruebas_resumen_d),
        ];
        renderizarPruebasPosi(data,labels);
    });
};

//Agrego codigo

//rendreizar el grafico
const renderizarPruebasSos =(data,labels)=>{
    
    var ctx = document.getElementById('pruebas_grafico_sos').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas',
                data: data,
                //aqui pueden editar los colores
                backgroundColor: [
                    'rgba(33, 36, 89, 0.7)',
                    'rgba(2, 100, 140, 0.7)',
                    'rgba(2, 140, 140, 0.7)',
                    'rgba(4, 191, 172, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(33, 36, 89, 1)',
                    'rgba(2, 100, 140, 1)',
                    'rgba(2, 140, 140, 1)',
                    'rgba(4, 191, 172, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],



                borderWidth: 1
            }]
        },
        options: {
           
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
           
        }
    });
}

//pero antes obtengo los datos del urrl.py
const getdataPruebasSos =()=>{
   
    fetch('/pruebas_resumen_genero_sospechosos')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const pruebas_resumen_d =results.pruebas_resumen_genero_sospechosos;
        const [labels,data]=[
            Object.keys(pruebas_resumen_d),
            Object.values(pruebas_resumen_d),
        ];
        //renderizo el grafico
        renderizarPruebasSos(data,labels);
    });
};
document.onload = getdataPruebasSos();
document.onload = setInterval( getdataPruebasSos, 6000);
//Finalizo
//este es el de inicio
document.onload = getdataPruebas();
document.onload =  getdataPruebasPosi();

//aqui pueden ajustar el tiempo de recarga
document.onload = setInterval( getdataPruebas, 6000);
document.onload =  setInterval( getdataPruebasPosi, 6000);
