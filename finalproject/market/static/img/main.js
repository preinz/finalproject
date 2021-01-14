
(function ($) {
    "use strict";


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);









let myForm = document.getElementById('myForm');
    let submit = document.getElementById("submit");
    submit.addEventListener('click', f_valid);

myForm.addEventListener = ('submit', function(e){
      let error;
      let inputName = document.getElementById('inputName')
      let inputEmail = document.getElementById('inputEmail')
      let inputMessage = document.getElementById('inputMessage')
      let missing_e = document.getElementById('missing_e');

   let inputs = document.getElementsByTagName('input');

   for (let i=0; i<inputs.length; i++){
       if(!inputs[i].value){
           error = "Please fill in all the Fields*"
        }
       else{
           alert('Message sent! Thank You')
       }
   }
       if(error){
           e.preventDefault();
           document.getElementById("error").innerHTML= error;
           return false;
       }
       else{
           alert('Mesaage sent! Thank You')
       }
})













