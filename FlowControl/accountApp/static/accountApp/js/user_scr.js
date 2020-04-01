const pass1 = document.getElementById('id_password1');
const pass = document.getElementById('id_password');
const pass2 = document.getElementById('id_password2');
const user = document.getElementById('id_username');
if (pass1 !== null){
	pass1.placeholder = "Пароль";
}
if (pass !== null){
	pass.placeholder = "Пароль";
}
if (pass2 !== null){
	pass2.placeholder = "Пароль";
}
if (user !== null){
	user.placeholder = "Логин";
}

const notes = document.getElementById('id_url_of_notes');
const disk = document.getElementById('id_url_of_disk');
const hw = document.getElementById('id_homework_link');
const aims = document.getElementById('id_aims_link');
const todo = document.getElementById('id_todo_link');
const name = document.getElementById('id_name');

notes.previousElementSibling.classList.add("col-5");
notes.previousElementSibling.classList.add("offset-1");

disk.previousElementSibling.classList.add("col-5");
disk.previousElementSibling.classList.add("offset-1");

hw.previousElementSibling.classList.add("col-5");
hw.previousElementSibling.classList.add("offset-1");

aims.previousElementSibling.classList.add("col-5");
aims.previousElementSibling.classList.add("offset-1");

todo.previousElementSibling.classList.add("col-5");
todo.previousElementSibling.classList.add("offset-1");

name.previousElementSibling.classList.add("col-5");
name.previousElementSibling.classList.add("offset-1");

notes.classList.add("col-5");
disk.classList.add("col-5");
hw.classList.add("col-5");
aims.classList.add("col-5");
todo.classList.add("col-5");
name.classList.add("col-5");
console.dir(notes);