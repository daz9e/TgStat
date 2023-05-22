import {upload} from "./upload.js";


upload('#file', {
	multi: true,
	accept: ['.docx', '.doc']
})



console.log('aboba');

//const inputElement = document.getElementById("input");
//inputElement.addEventListener("change", handleFiles, false);
//function handleFiles() {
//  const fileList = this.files; /* now you can work with the file list */
//  console.log(fileList);
//}




// форма в которой храним данные
let formData = new FormData();

// Реагируем когда что-то перетаскивают
dropzone.addEventListener('dragenter', function(){
  dropzone.className="hover";
});

// Перестаём реигировать когда перетаскивание закончилось
['drop', 'dragleave'].forEach(eventName => dropzone.addEventListener(eventName, function(){
  dropzone.className="";
}));

// начинаем обрабатывать когда что-то сбросили нам
['drop', 'dragover'].forEach(eventName => dropzone.addEventListener(eventName, function(e){
  // отменяем стандартные действия
  e.preventDefault()
  e.stopPropagation()
  
  // тут у нас лежат перетащенные файлы
  let files = e.dataTransfer.files;

  // но это не мессив, поэтому делаем массивом
  files = [...files];
 
  
  files.forEach(file => {
    // переадаём файл форме
    formData.append('file', file);

    const title = document.querySelector('.area__text__title')
	const subtitle = document.querySelector('.area__text__subtitle')
	const image = document.querySelector('.area__icon')
	const parent1 = title.parentNode
	const parent2 = subtitle.parentNode
	const parent3 = image.parentNode

	parent1.removeChild(title)
	parent2.removeChild(subtitle)
	parent3.removeChild(image)
    // начинаем делать предпросмотр
    // именно тут, просто создаём html-элементы и кидаем их настраницу
    let preview = document.createElement('li');
    file_list.appendChild(preview);
    
    // в идеале нужно проверить является ли файл картинкой
    //makePreview(file).then(docx => {
    //  let img = document.createElement('div');
    //  img.textContent = 'Hello, World!';
    //  preview.appendChild(img);
    //});
    
    // показываем кнопку "Отправить"
    submitBtn.className="buttons__upload button";
    
  });
  
}, false));

// вот тут, через FileReader читаем изображание
function makePreview(file){
  let fr = new FileReader();
  
  return new Promise(resolve => {
    fr.readAsDataURL(file);
    // и когда оно готово, отдаём ответ
    fr.onloadend = () => resolve(fr.result)
  });
}

// отправка всего на сервер
submitBtn.onclick = function() {
  let url = null; // URL куда отправляем файлы
  fetch(url, {
    method: 'POST',
    body: formData
  })
  // всё заргузилось
  .then(resp => console.log(resp))
  // какие-то проблемы
  .catch(err => console.error(err))
}