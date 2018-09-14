$(document).ready(function(){

    $('#id_symptoms').multiselect({
        maxHeight: 300,
        buttonWidth: '100%',
        numberDisplayed: 5,
        enableCaseInsensitiveFiltering: true,
        includeSelectAllOption: true,
        nonSelectedText: 'Choose Symptoms',
        onChange: function(option, checked) {
            var count = $("#id_symptoms :checked").length;
            if(count != 0)
                $('#button_submit').prop('disabled', false);
            else
                $('#button_submit').prop('disabled', true);
        },
        onSelectAll: function() {
            $('#button_submit').prop('disabled', false);
        },
        onDeselectAll: function() {
            $('#button_submit').prop('disabled', true);
        }
    });

    
});

    
