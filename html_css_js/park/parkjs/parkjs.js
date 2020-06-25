$('.learn').on('click', showsidebar);
var state = true;

function showsidebar() {
	if(state){
		$('div#side-navbar').stop().animate({width:'250px'},500);

	}else{
		$('div#side-navbar').stop().animate({width:'0px'},500);

	}
	state = !state;
}
showsidebar();


