$(function () {


    $(document).ready(function () {
        $('.test-slider').slick({
            nextArrow: '<button class="test-slider__slider-btn test-slider__slider-btnnext "><img src="../media/images/arrow-right-slider.svg" alt=""></button>',
            prevArrow: false,
            slidesToShow: 4,
            slideToScroll: 1,

        });
    });

    $(document).ready(function () {
        $('.test-slider__item').tilt({
            speed: 500,
            maxTilt: 10,


        });


    });





    var dt = new DataTransfer();

    $('.input-file input[type=file]').on('change', function(){
        let $files_list = $(this).closest('.input-file').next();
        $files_list.empty();

        for(var i = 0; i < this.files.length; i++){
            let file = this.files.item(i);
            dt.items.add(file);

            let reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = function(){
               $('.lol-image').attr("src", reader.result)
            }
        };
        this.files = dt.files;
    });

    function removeFilesItem(target){
        let name = $(target).prev().text();
        let input = $(target).closest('.input-file-row').find('input[type=file]');
        $(target).closest('.input-file-list-item').remove();
        for(let i = 0; i < dt.items.length; i++){
            if(name === dt.items[i].getAsFile().name){
            dt.items.remove(i);
            }
        }
        input[0].files = dt.files;
    }








    $(function(){
        var nav = $('.themes__wrapper'),
            animateTime = 500,
            navLink = $('.toggle_themes_list');
        navLink.click(function(){
            if ( $(".toggle_themes_list").hasClass("active") ){
                $(".toggle_themes_list").removeClass("active")

                $('.toggle_themes_list').text('Показать все темы');
             nav.stop().animate({ height: '100' }, animateTime);

          } else {
            $(".toggle_themes_list").addClass("active")
            $('.toggle_themes_list').text("Скрыть темы");
           autoHeightAnimate(nav, animateTime);

          }
        });
      })


    function autoHeightAnimate(element, time){
        var curHeight = element.height(), // Get Default Height
          autoHeight = element.css('height', 'auto').height(); // Get Auto Height
            element.height(curHeight); // Reset to Default Height
            element.stop().animate({ height: autoHeight }, time); // Animate to Auto Height
  }






    $(document).ready(function (){

        animateTime = 500,
        navLink = $('.btn-one');

    navLink.click(function(){
    var nav =  $($(this).parent().siblings().find('.vacancy__input'))

        if ( $(nav).hasClass("active") ){

            $(nav).prop('readonly', true);


         nav.stop().animate({ height: '0' }, animateTime);
        $(nav).removeClass("active")
      } else {
        $(nav).addClass("active")
       autoHeightAnimate(nav, animateTime);
       $(nav).prop('readonly', false);
      }


    btn= $($(this).parent().siblings().find('.btn-22'))
    if ( $(btn).hasClass("active") ){

        $(btn).prop('readonly', true);


     btn.stop().animate({ height: '0' }, animateTime);
    $(btn).removeClass("active")
  } else {
    $(btn).addClass("active")
   autoHeightAnimate(btn, animateTime);
   $(btn).prop('readonly', false);
  }


    });

  })

//    $(function() {
//
//
//        let container = document.querySelector("#form-container")
//        let addButton = document.querySelector("#add-form")
//        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
//
//        var hasRun = false;
//
//        addButton.addEventListener('click', addForm)
//
//        function addForm(e){
//            e.preventDefault()
//            let testForm = document.querySelectorAll(".test-form")
//            let formNum = testForm.length-1
////            console.log(formNum);
//            let newForm = testForm[0].cloneNode(true)
//
//            let formRegex = RegExp(`form-(\\d){1}-`,'g')
//
//            formNum++
//            newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
//             newForm.innerHTML = newForm.innerHTML.replace('question__input', 'check')
//
// console.log(newForm.innerHTML);
//            container.insertBefore(newForm, addButton)
//  var nav =  $($(newForm).find('.answer__input'))
//
// console.log(nav);
//
//$(nav).val('');
//
//            totalForms.setAttribute('value', `${formNum+1}`)
////  $('.check').styler();
//
//
//                    }
//
//
//
//    });





$(document).on('click', '.check', function(){



    if ($(this).hasClass('checked'))
    {
  s=$(this).find('input:checkbox')

        $(s).prop('checked', false)
 console.log($(s).is(':checked'));
	    $(this).removeClass('checked')

		}

		else
		{
  s=$(this).find('input:checkbox')
		$(s).prop('checked', true)

	$(this).addClass('checked')
	 console.log($(s).is(':checked'));


		}
});

      $(function() {

            $('.question__input').styler();

        });



    $(function() {

        $('.js-example-basic-single').select2({
            placeholder: "Выберите тему",
            allowClear: true,
            closeOnSelect: false,

        });

    });






    $('.theme__add').on('click touchstart', function (e) {



        if (
            $(".test-serch__form").hasClass('active')) {

                $(".test-serch__form").removeClass('active');
        }
        else {
            $(".test-serch__form").slideToggle('fast,easing');
            $(".test-serch__form").removeClass('active');
        }

    });



// наведение на 1 звезду
    $(".rait-1").mouseout(function(e)
    {
  $(".rait-1").css("fill", "none");
    });
	$(".rait-1").mousemove(function(e){
   $(".rait-1").css("fill", "#FFCA28");
   $(".rait-1").css("transition", "fill 3s");
});



// наведение на 2 звезду
$(".rait-2").mouseout(function(e)
{
$(".rait-1").css("fill", "none");
$(".rait-2").css("fill", "none");
});
$(".rait-2").mousemove(function(e){
$(".rait-1").css("fill", "#FFCA28");
$(".rait-2").css("fill", "#FFCA28");
});


// наведение на 3 звезду
$(".rait-3").mouseout(function(e)
{

$(".rait-1").css("fill", "none");
$(".rait-2").css("fill", "none");
$(".rait-3").css("fill", "none");

});

$(".rait-3").mousemove(function(e){

$(".rait-1").css("fill", "#FFCA28");
$(".rait-2").css("fill", "#FFCA28");
$(".rait-3").css("fill", "#FFCA28");

});



// наведение на 4 звезду
$(".rait-4").mouseout(function(e)
{

$(".rait-1").css("fill", "none");
$(".rait-2").css("fill", "none");
$(".rait-3").css("fill", "none");
$(".rait-4").css("fill", "none");

});

$(".rait-4").mousemove(function(e){

$(".rait-1").css("fill", "#FFCA28");
$(".rait-2").css("fill", "#FFCA28");
$(".rait-3").css("fill", "#FFCA28");
$(".rait-4").css("fill", "#FFCA28");

});


// наведение на 5 звезду
$(".rait-5").mouseout(function(e)
{
$(".rait-1").css("fill", "none");
$(".rait-2").css("fill", "none");
$(".rait-3").css("fill", "none");
$(".rait-4").css("fill", "none");
$(".rait-5").css("fill", "none");
});
$(".rait-5").mousemove(function(e){
$(".rait-1").css("fill", "#FFCA28");
$(".rait-2").css("fill", "#FFCA28");
$(".rait-3").css("fill", "#FFCA28");
$(".rait-4").css("fill", "#FFCA28");
$(".rait-5").css("fill", "#FFCA28");
});






$('body').on('click', '.password__control', function(){

    var button = $(this).parent().find('.password__input')

    console.log(button);
	if ($(button).attr('type') == 'password'){
		$(this).addClass('view');

		$(button).attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$(button).attr('type', 'password');
	}
	return false;
});





      $("#CallPasswordChangeButton").on('click', function (e) {
            e.preventDefault(); // avoid to execute the actual submit of the form.
            var form = $('#PasswordChnageForm');
            $.ajax({
                type: 'Post',
                url: "{% url 'auth:change_password' %}",
                data: form.serialize(),
                success: function (data) {
                    $('#password_change').empty().html(data);
                }
            });
        });






});












// $('.input-file input[type=file]').on('change', function(){
//     let $files_list = $(this).closest('.input-file').next();
//     $files_list.empty();

//     for(var i = 0; i < this.files.length; i++){
//         let file = this.files.item(i);
//         dt.items.add(file);

//         let reader = new FileReader();
//         reader.readAsDataURL(file);
//         reader.onloadend = function(){
//             let new_file_input = '<div class="input-file-list-item">' +
//                 '<img class="input-file-list-img profile__avatar" src="' + reader.result + '">' +
//                '<input type="submit" class="img-input" value="сохранить">'
//             '</div>';
//             $files_list.append(new_file_input);
//         }
//     };
//     this.files = dt.files;
// });

// function removeFilesItem(target){
//     let name = $(target).prev().text();
//     let input = $(target).closest('.input-file-row').find('input[type=file]');
//     $(target).closest('.input-file-list-item').remove();
//     for(let i = 0; i < dt.items.length; i++){
//         if(name === dt.items[i].getAsFile().name){
//             dt.items.remove(i);
//         }
//     }
//     input[0].files = dt.files;
// }