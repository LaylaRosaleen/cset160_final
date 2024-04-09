let teacheremail = "teacher"
let teacherpass = "teacher"

function signup(){
    let email = document.getElementById("email").value
    let pass = document.getElementById("pass").value

    localStorage.setItem(email, pass)
}

function login(){
    let email = document.getElementById("email").value
    let pass = document.getElementById("pass").value

    if(email == teacheremail){
        if(pass == teacherpass){
            location.replace("teacher.html")
        }else{
            alert("wrong password")

        }
    }else if(localStorage.getItem(email)){
        if(pass === localStorage.getItem(email)){
            location.replace("student.html")
        }
        else{
            alert("wrong password")
        }
    }
    else {
        alert("User not found")
    }
}