$(document).ready(function() {
			$('#example').DataTable();
		  } );
$(document).ready(function() {
			var table = $('#example2').DataTable( {
				lengthChange: true,
				pageLength: 100,
				buttons: [ 'copy', 'excel', 'pdf', 'print']
			} );

			table.buttons().container()
				.appendTo( '#example2_wrapper .col-md-6:eq(0)' );
		} );

