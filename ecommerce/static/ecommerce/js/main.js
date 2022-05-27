/*price range*/

 $('#sl2').slider();

	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};	
		
/*scroll to top*/

$(document).ready(function(){
	$(function () {
		$.scrollUp({
	        scrollName: 'scrollUp', // Element ID
	        scrollDistance: 300, // Distance from top/bottom before showing element (px)
	        scrollFrom: 'top', // 'top' or 'bottom'
	        scrollSpeed: 300, // Speed back to top (ms)
	        easingType: 'linear', // Scroll to top easing (see http://easings.net/)
	        animation: 'fade', // Fade, slide, none
	        animationSpeed: 200, // Animation in speed (ms)
	        scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
					//scrollTarget: false, // Set a custom target element for scrolling to the top
	        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
	        scrollTitle: false, // Set a custom <a> title if required.
	        scrollImg: false, // Set true to use image
	        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	        zIndex: 2147483647 // Z-Index for the overlay
		});
	});
});


	console.log('working...');

	if(localStorage.getItem('cart')==null)
	{
		var cart= {};
	}
	else
	{
		cart=JSON.parse(localStorage.getItem('cart'));
		document.getElementById('cart').innerHTML=Object.keys(cart).length;
		updateCart(cart);
	}
				
	$('.cart').click(function()
	{
	console.log('clicked');
	var idstr = this.id.toString();
	console.log(idstr);
		if (cart[idstr] !=undefined){
			cart[idstr] = cart[idstr] + 1;	
		}
		else{
			cart[idstr] = 1;
		}

	console.log(cart);
	localStorage.setItem('cart',JSON.stringify(cart));
	document.getElementById('cart').innerHTML=Object.keys(cart).length;


});	
	function updateCart(cart) {
		// for (var item in cart) {
		// 		document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'> - </button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
		// }
			localStorage.setItem('cart', JSON.stringify(cart));
			document.getElementById('cart').innerHTML = Object.keys(cart).length;
			console.log(cart);
		}   
	$('.cart_quantity_up').click(function(){
		var id=$(this).attr("pid").toString();
		var eml=$(this).parentNodechildren[2]
		console.log("--- id ---",id);
		$.ajax({
			type: "GET",
			url: "/pluscart",
			data: {
				prod_id:id
			},
			success: function (data){
				eml.innerText = data.quantity
				console.log("--- data ---",data)	
				console.log("--- success ---",success)			 
		 
			}
		})
		
				 
 
	})
	
	
	$('.cart_quantity_down').click(function(){
		var id=$(this).attr("pid").toString();
		console.log(id);
		
	})

	

	
