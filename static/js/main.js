window.onload = () => {
    preloader = document.querySelector('#preloader');
    preloader.style.visibility = 'hidden';
    preloader.style.opacity = 0;
}

let user=document.getElementById("exampleModalLabel");
let tableTr=document.querySelectorAll(".tabletr");
let sendSms=document.getElementById('sendSms');
let checkSms=document.getElementById('checksms');
let tastiqlashBtn=document.getElementById('tastiqlashbtn');
let images;
let img_count = 0;



function send_sms(data){
    checkSms.addEventListener('input',()=>{
        user_text=checkSms.value
        if(user_text==data){
            tastiqlashBtn.disabled = false;
        }else{
            tastiqlashBtn.disabled = true;        
        }
    })
}

tableTr.forEach(tr=>{
    tr.addEventListener('click',()=>{
        user.textContent=`${tr.childNodes[3].textContent}: ${tr.childNodes[7].textContent}`;
        send=document.createAttribute('data-send-sms')
        send.value=tr.childNodes[7].textContent
        sendSms.setAttributeNode(send)
    });
})

function showImg(imgs){
    images = imgs
    let img_modal = document.querySelector('.img_modal');
    img_modal.style.display = 'block';
    img_modal.innerHTML = `<div class="d-flex justify-content-md-around justify-content-between align-items-center h-100">
                                <i onclick="img_left_right(event)"  class="fa-solid fa-angle-left fa-2x text-light pointer"></i>
                                <i onclick="img_left_right(event)"  class="fa-solid fa-angle-right fa-2x text-light pointer"></i>
                            </div>
                            <img src="/media/${imgs[0].fields.img}" alt="">
                            <span class="img_modal_close" onclick="closeImg()" style="display:block;"><i class="fa-solid fa-xmark"></i></span>
                            `
    img_modal.style.position = 'absolute';
}

function img_left_right(e){
    let img_tag = document.querySelector('.img_modal img');
    if(e.target.classList.contains('fa-angle-left')){
        img_count--
        if(img_count<0){
            img_count=images.length-1
            img_tag.src='/media/' + images[img_count].fields.img
        } else{
            img_tag.src='/media/' + images[img_count].fields.img
        }
    } else{
        img_count++
        if(img_count>images.length-1){
            img_count=0
            img_tag.src='/media/' + images[0].fields.img
        } else{
            img_tag.src='/media/' + images[img_count].fields.img
        }
    }
}


function closeImg(){
    document.querySelector('.img_modal').style.display = 'none'
}


function graficPageRankFilter(e){
    let list_group_ranks = document.querySelectorAll('.list-group-item');
    list_group_ranks.forEach((item) => {
        item.style.display = 'block'
        if (item.dataset.rank && item.dataset.rank != e.target.value) {
            item.style.display = 'none'
        }
        if (e.target.value == 'all'){
            item.style.display = 'block'
        }
    })
}


function jadvalDateFilter(e){
    let date = 'no'
    if (e.target.value){
        date = e.target.value
    }
    jadvalFiltering(null, null, date)
}
function jadvalNameFilter(e){
    jadvalFiltering(e.target.value, null, null)
}
function jadvalRankFilter(e){
    jadvalFiltering(null, e.target.value, null)
}


function jadvalFiltering(name, rank, date){
    let jadval_table = document.querySelectorAll('.jadval_items')
    if (name){
        jadval_table.forEach((item) => {
            item.classList.remove('d-none')
            if (item.childNodes[2].textContent.match(name)) {
                item.classList.remove('d-none')
            } else{
                item.classList.add('d-none')
            }
        })
    } else if (rank){
        jadval_table.forEach((item) => {
            item.classList.remove('d-none')
            if(rank=='all'){
                item.classList.remove('d-none')
            }else if (item.childNodes[4].textContent.match(rank)){
                item.classList.remove('d-none')
            }else{
                item.classList.add('d-none')
            }
            
        })
        
    } else if (date){
        jadval_table.forEach((item) => {
            item.classList.remove('d-none')
            if (date == 'no'){
                item.classList.remove('d-none')
            }else if (Date.parse(item.childNodes[11].textContent) != Date.parse(date)) {
                item.classList.add('d-none')
            }
        })
    }
}








//   now Lets make our calendar dynamic using some javascript

let dayList = document.querySelector('.days');
let monthName = document.querySelector('.month-name');
let yearName = document.querySelector('.year');
let prev = document.querySelector('.prev');
let next = document.querySelector('.next');

// lets create an Date object

let dt = new Date();
let month = dt.getMonth()+1 //as it will return value between 0-11 so to make it 1-12 we add 1 to it
let year = dt.getFullYear();
let currentDay = dt.getDate();

// make an array of month name to map with the month value we obtained using getMonth()
let monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'july', 'August', 'September', 'October', 'November', 'December']


// now lets handle the previous and next button click
prev.addEventListener('click',event=>{
    if(month===1){
        month =12;
        month-=1;
    }else{
        month-=1;
    }
    calendar();
})

next.addEventListener('click',event=>{
    if(month===12){
        month =1;
        month+=1;
    }else{
        month+=1;
    }
    calendar();
})
// now lets make a calendar function

const calendar = ()=>{
    monthName.innerHTML = monthNames[month-1];
    yearName.innerHTML = year;
    dayList.innerHTML = ''
    
    daysInMonth = new Date(year, month, 0).getDate(); //get toatl number of days in a particular month


    //  but still there is a problem
    // you can see that for every month the date starts from monday
    // it should not be as that
    // date of a new month should start from the next immediate dat from when the previous month ends
    // so lets match that pattern by adding gaps before the starting of the day in month

    // get day number at which the current month start (0 for sunday, 6 for saturday)

    dayNumber = new Date(year,month-1,1).getDay();
    let gaps
    if (dayNumber === 0) {
        gaps = 6
    }else{
        gaps = dayNumber - 1;
        // Ex:: if it is monday dayNumber = 1, so gaps = 1-1 = 0;
        // if it is thursdat dayNumber = 4, so gaps = 4-1 = 3;
    }

    for(day = -gaps + 1 ;day<=daysInMonth; day++){
        const days = document.createElement('li');
        if(day<=0){
            days.innerHTML = "";
            dayList.appendChild(days);
        } else if (day===currentDay&&month===dt.getMonth()+1 && year===dt.getFullYear()){
            //make this date as active as it is current date i.e. today
            days.setAttribute('class','active');
            days.innerHTML = day;
            dayList.appendChild(days)
        }
        else{
            days.innerHTML = day;
            dayList.appendChild(days);
        }
    }
}

