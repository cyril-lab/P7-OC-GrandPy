$(document).ready(function(){
    $(function(){
        $('#form-question').submit(function(e){
            e.preventDefault();
        var formulaire = $(this);
        var post_url = '/getAnswer';
        var post_data = formulaire.serialize();
        //I test if the form field is not empty
        if ($('#formtexte').val() !="") {
            $.post(post_url, 
                post_data, 
                function(data, status){ 
                console.log(data, status);
                //I get the question
                var question = $('#formtexte').val();
                //question display
                var $question = $("<div class='chat_right'><p>"+question+"</p></div>");
                //deletion of the form
                $('#form-question').get(0).reset();
                //adding the question to the screen
                $('#chat').append($question);
                //loader
                $('.loader').fadeIn();
                //adding the answer to the screen
                var answer_papy = JSON.parse(data);
                //answer api google map 
                var $answer_address = $("<div class='chat_left'><p>Bien sûr mon poussin ! La voici : "+answer_papy.address+"</p></div>");
                //answer wikipedia
                var $answer_wiki = $("<div class='chat_left'><p>Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? "+
                    answer_papy.wiki_answer+"</p><a href='https://fr.wikipedia.org/wiki/"+
                    answer_papy.article_title+"'>Lien Wikipedia</a></div>");
                //answer latitude
                var latitude = answer_papy.latitude
                //answer longitude
                var longitude = answer_papy.longitude
                //answer address display
                $('#chat').append($answer_address);
                setTimeout(function() {
                    $('#chat').append($answer_wiki);
                    //to display the last comment
                    $(document).scrollTop($(document).height());
                  }, 2000);
                //answer wiki display
                //$('#chat').append($answer_wiki);
                //location
                var location = {lat: latitude, lng: longitude};
                // The map
                var map = new google.maps.Map(
                    document.getElementById('map'), {zoom: 10, center: location});
                // The marker
                var marker = new google.maps.Marker({position: location, map: map});
                //to display the last comment
                $(document).scrollTop($(document).height());
                //Hide loader
                $('.loader').fadeOut('fast');
            });
            };
        });
    });

});


