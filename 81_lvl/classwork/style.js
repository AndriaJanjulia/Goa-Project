//let number = prompt("enter number:");

//if (number > 10000) {
    //alert("რიცხვი 10000 ზე მეტია");
//} else {
    //alert("რიცხვი 10000 ნაკლებია");
//}




for (let i = 1; i <= 100; i++) {
    if (i === 50) {
        break;
    }
    if (i % 4 == 0) {
        continue;
    }
    console.log(i);
}