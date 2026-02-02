const addItem = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

addItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.appendChild(li);
});

