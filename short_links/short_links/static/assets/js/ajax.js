
// Создание ссылки
$(document).ready(function () {
        $('#addLinkForm').submit(function () {
            $.ajax({
                data: $(this).serialize(),
                type: $(this).attr('method'),
                url: '/info/generate',
                success: function (response) {
                    $('input').attr('readonly', 'readonly');
                    $('.submit').css('display', 'none');
                    $('.reload').css('display', 'block');
                    $("input[name='link_agent']" ).val('https://bankrotstvo-razdorov.ru/'+response);
                },
                error: function (response) {
                    alert(response.responseJSON.errors);
                    console.log(response.responseJSON.errors)
                }
            });
            return false;
        });
    })

	var clipboard = new ClipboardJS('#button-copy', {
	text: function(trigger) {
		return document.getElementById('linkForAgent').value;
	}
});
