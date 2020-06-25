/* 
$('#home').on('click', clickHome);
//clickHome 함수로 넘어가는데 뒤에 ; 안붙힘.
$('#seoul').on('click', clickSeoul);
$('#tokyo').on('click', clickTokyo);
$('#paris').on('click', clickParis);

$('#photo').on('mouseenter', mouseEnterPhoto);
$('#photo').on('mouseleave', mouseLeavePhoto);

//사용자가 키보드 누르는 이벤트
//페이지 전체의 이벤트 document
$(document).on('keydown', procssKeyEvent);



// 사진을 바꿔주는 함수
function clickHome() {
  document.getElementById('photo').src = 'images/home.png';
  document.getElementById('home').style.fontWeight = 'bold';
  document.getElementById('seoul').style.fontWeight = 'normal';
  document.getElementById('tokyo').style.fontWeight = 'normal';
  document.getElementById('paris').style.fontWeight = 'normal';
}

function clickSeoul() {
  //document.getElementById('photo').src = 'images/seoul.png';
  $('#photo').attr('src', 'images/seoul.png');

  //document.getElementById('home').style.fontWeight = 'normal';
  $('#home').css('font-weight', 'normal');
  //document.getElementById('seoul').style.fontWeight = 'bold';
  $('#seoul').css('font-weight', 'bold');

  document.getElementById('tokyo').style.fontWeight = 'normal';
  document.getElementById('paris').style.fontWeight = 'normal';
}

function clickTokyo() {
  document.getElementById('photo').src = 'images/tokyo.png';
  document.getElementById('home').style.fontWeight = 'normal';
  document.getElementById('seoul').style.fontWeight = 'normal';
  document.getElementById('tokyo').style.fontWeight = 'bold';
  document.getElementById('paris').style.fontWeight = 'normal';
}

function clickParis() {
  document.getElementById('photo').src = 'images/paris.png';
  document.getElementById('home').style.fontWeight = 'normal';
  document.getElementById('seoul').style.fontWeight = 'normal';
  document.getElementById('tokyo').style.fontWeight = 'normal';
  document.getElementById('paris').style.fontWeight = 'bold';
}
//사진에 그림자 
function mouseEnterPhoto() {
  $('#photo').css('box-shadow', '5px 10px');
}
function mouseLeavePhoto() {
  $('#photo').css('box-shadow', 'none');
}

function procssKeyEvent(event) {
  if (event.key === '1') {
  	clickHome();
  } else if (event['key'] === '2') {
  	clickSeoul();
  } else if (event['key'] === '3') {
  	clickTokyo();
  } else if (event['key'] === '4') {
  	clickParis();
  }
}
*/
// 전부 Jquery로 바꿈 .
$('#menu a').on('click', selectMenu);
$(document).on('keydown', selectMenu);

function selectMenu(event) {
  var targetId = '';
  if(event.type === 'click') {
    targetId = event.currentTarget.id;
  }else if(event.type === 'keydown') {
    if(event.key === '1') {
      targetId = 'home';
    }else if(event.key === '2') {
      targetId = 'seoul';
    }else if(event.key === '3') {
      targetId = 'tokyo';
    }else if(event.key === '4') {
      targetId = 'paris';
    }
  }
  $('#photo').fadeOut(200, display_fn);
  function display_fn() {
    $('#photo').attr('src', 'images/'+ targetId +'.png');
    $('#photo').fadeIn(700);
    $('#menu a').css('font-weight', 'normal');
    $('#'+targetId).css('font-weight', 'bold');
  }


}
