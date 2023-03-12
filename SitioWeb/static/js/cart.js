var updateBtns = documents.getElemenstsByClassName('uptade-cart')

for (var i =0 ; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productoId =this.dataset.producto
        var action =this.dataset.action
        console.log('productoId:', productoId, 'action:', action)
    })
}