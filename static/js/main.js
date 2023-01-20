let areaSelect = document.querySelector('#select')
let save_grafic = document.querySelector('#save_grafic')
let doctors_list = document.querySelectorAll('.doctors_list')

areaSelect.addEventListener('change',(e)=>{
    getStreets(e.target.value)
});

let areaSelect2 = document.querySelector('#select2')

areaSelect2.addEventListener('change',(e)=>{
    getAddress(e.target.value)
})