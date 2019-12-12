function toggleSnackbar(message) {
    let snackbar = document.createElement('div')
    snackbar.setAttribute('id','snackbar')
    let doneIcon = document.createElement('i')
    doneIcon.classList.add('material-icons')
    doneIcon.innerHTML = "done";  

    document.querySelector('body').append(snackbar)
    snackbar.append(message)





    snackbar.className = "show";
    setTimeout(function(){ snackbar.className = snackbar.className.replace("show", ""); snackbar.remove() }, 3000);
 
  }

function toggleModalWindow(message){

    let modal = document.createElement('div')
    modal.classList.add('modal')
    let exitSpan = document.createElement('span')
    exitSpan.classList.add('close')
    exitSpan.innerHTML = "&times;";  
    let modalContent = document.createElement('div')
    modalContent.classList.add('modal-content')

    modal.style.display = "block";


    document.querySelector('body').append(modal)
    modal.append(modalContent)
    modalContent.append(exitSpan)
    modalContent.append(message)

    exitSpan.onclick = function() {
        modal.style.display = "none";
        modal.remove()
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }
}