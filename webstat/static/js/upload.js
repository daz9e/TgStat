function formatBytes(bytes, decimals = 2) {
    if (!+bytes) return '0 Bytes'
    const k = 1024
    const dm = decimals < 0 ? 0 : decimals
    const sizes = ['Bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

    const i = Math.floor(Math.log(bytes) / Math.log(k))

    return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
}

export function upload(selektor, options = {}) {
	let files = []
	const input = document.querySelector(selektor) //ищем инпут
	const preview = document.createElement('div')

	preview.classList.add('preview') //добавляем в эелемент класс

	const open = document.createElement('button') // создаем кнопку
	open.classList.add('btn') //добавляем в эелемент класс
	open.textContent = 'Open'

	if (options.multi) { //проверяем, можно ли добавлять несколько файлов
		input.setAttribute('multiple', true)
	}
	if (options.accept && Array.isArray(options.accept)) {
		input.setAttribute('accept', options.accept.join(','))
	}

	input.insertAdjacentElement('afterend', open)
	input.insertAdjacentElement('afterend', preview) // добавляем элемент после конца инпута

	const triggerInput = () => input.click()

	const changeHandler = event => { //проверка на наличие файла
		if (!event.target.files.length) {
			return
		}

		 files = Array.from(event.target.files) //делвем массив из списка
		
		preview.innerHTML = ''
		files.forEach(file => {
			//if (!file.type.match('image')) { // праверка на картинку
			//	return
			//}

			const reader = new FileReader()
							const title = document.querySelector('.area__text__title') //удаление лишнего
							const subtitle = document.querySelector('.area__text__subtitle')
							const image = document.querySelector('.area__icon')
							const parent1 = title.parentNode
							const parent2 = subtitle.parentNode
							const parent3 = image.parentNode

							parent1.removeChild(title)
							parent2.removeChild(subtitle)
							parent3.removeChild(image)
			reader.onload = ev => {
				//const src = ev.target.result
				//console.log(ev.target.result)  //получаем код картинки
				//input.insertAdjacentHTML('afterend', `<img src="${ev.target.result}" />`) //вставляем закодированную картинку в тег img
				preview.insertAdjacentHTML('afterbegin', `
					<div class="preview-image">
					<div class="preview-remove" data-name="${file.name}">&times;</div>  
						<img src="./static/img/1.jpg" alt="${file.name}" />
							<div class="preview-info">
								<div class="preview-info-name">Name: ${file.name}</div>
								<div class="preview-info-size">Size: ${formatBytes(file.size)}</div>
							</div>
					</div>
				`)
			}

			reader.readAsDataURL(file)
		})
	}

	const removeHandler = event => {
		
		if (!event.target.dataset.name) {
			return
		}
		
		const {name} = event.target.dataset
		files = files.filter(file => file.name !== name)

		const block = preview.querySelector(`[data-name="${name}"]`).closest('.preview-image')
		block.remove()
		location.reload()
	}

	open.addEventListener('click', triggerInput)
	input.addEventListener('change', changeHandler)
	preview.addEventListener('click', removeHandler)
}