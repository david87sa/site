var currentSection = 0;
var sections = document.querySelectorAll('.section');


window.addEventListener("load", () => {
    function sendData(form) {
      const XHR = new XMLHttpRequest();
  
      // Bind the FormData object and the form element
      const FD = new FormData(form);
  
      // Define what happens on successful data submission
      XHR.addEventListener("load", (event) => {
        //alert(event.target.responseText);
        if(event.target.responseText == 'Y'){
            document.getElementById('confirmed-input-yes').classList.add('selected');
            document.getElementById('confirmed-input-no').classList.remove('selected');
        }else{
            document.getElementById('confirmed-input-no').classList.add('selected');
            document.getElementById('confirmed-input-yes').classList.remove('selected');
        }
        window.setTimeout(function(){

            nextSection = currentSection +1;
        
            changeSection(currentSection,nextSection)
        },1000)
      });
  
      // Define what happens in case of error
      XHR.addEventListener("error", (event) => {
        alert('Oops! Something went wrong.');
      });
  
      // Set up our request
      XHR.open("POST", location.protocol + '//' + window.location.host+"/sitesapp/confirmation/");
  
      // The data sent is what the user provided in the form
      XHR.send(FD);
    }
  
    // Get the form element
    const formYes = document.getElementById("confirm-yes");
    const formNo = document.getElementById("confirm-no");
  
    // Add 'submit' event handler
    formYes.addEventListener("submit", (event) => {
        event.preventDefault();
        sendData(formYes);
    });    // Add 'submit' event handler
    formNo.addEventListener("submit", (event) => {
        event.preventDefault();
        sendData(formNo);
    });
  });



/*for (i=0;i<sections.length;++i){
    sections[i].addEventListener('click',function(){
        nextSection = currentSection +1;
        if(nextSection>=sections.length){
            nextSection=0
        }
        changeSection(currentSection,nextSection)
    });
}*/
function changeSection(from,to){
    sections[from].classList.remove('visible');
    sections[from].classList.add('hidden');
    sections[to].classList.remove('hidden');
    sections[to].classList.add('visible');
    if(to == 3 ){
        document.getElementById("phrase-4").classList.add("visible");
        document.getElementById("phrase-4-2").classList.remove("visible");
    }
    if(to == 4 ){
        document.getElementById("phrase-5").classList.remove("visible");
        document.getElementById("phrase-5-2").classList.add("visible");
    }
    currentSection=to;
    window.setTimeout(scheduler,5000)

}
var scheduler = function(){

    nextSection = currentSection +1;
    if(nextSection>=sections.length){
        nextSection=0;
    }
    if(currentSection==2){
        return;
    }

    changeSection(currentSection,nextSection)
}
window.setTimeout(scheduler,5000)