# from django.test import TestCase

# # Create your tests here.
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="utf-8">
# <meta http-equiv="X-UA-Compatible" content="IE=edge">
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <title>Bootstrap CRUD Data Table for Database with Modal Form</title>
# <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
# <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
# <style>
#     body {
#         color: #566787;
# 		background: #f5f5f5;
# 		font-family: 'Varela Round', sans-serif;
# 		font-size: 13px;
# 	}
# 	.table-wrapper {
#         background: #fff;
#         padding: 20px 25px;
#         margin: 30px 0;
# 		border-radius: 3px;
#         box-shadow: 0 1px 1px rgba(0,0,0,.05);
#     }
# 	.table-title {        
# 		padding-bottom: 15px;
# 		background: #435d7d;
# 		color: #fff;
# 		padding: 16px 30px;
# 		margin: -20px -25px 10px;
# 		border-radius: 3px 3px 0 0;
#     }
#     .table-title h2 {
# 		margin: 5px 0 0;
# 		font-size: 24px;
# 	}
# 	.table-title .btn-group {
# 		float: right;
# 	}
# 	.table-title .btn {
# 		color: #fff;
# 		float: right;
# 		font-size: 13px;
# 		border: none;
# 		min-width: 50px;
# 		border-radius: 2px;
# 		border: none;
# 		outline: none !important;
# 		margin-left: 10px;
# 	}
# 	.table-title .btn i {
# 		float: left;
# 		font-size: 21px;
# 		margin-right: 5px;
# 	}
# 	.table-title .btn span {
# 		float: left;
# 		margin-top: 2px;
# 	}
#     table.table tr th, table.table tr td {
#         border-color: #e9e9e9;
# 		padding: 12px 15px;
# 		vertical-align: middle;
#     }
# 	table.table tr th:first-child {
# 		width: 60px;
# 	}
# 	table.table tr th:last-child {
# 		width: 100px;
# 	}
#     table.table-striped tbody tr:nth-of-type(odd) {
#     	background-color: #fcfcfc;
# 	}
# 	table.table-striped.table-hover tbody tr:hover {
# 		background: #f5f5f5;
# 	}
#     table.table th i {
#         font-size: 13px;
#         margin: 0 5px;
#         cursor: pointer;
#     }	
#     table.table td:last-child i {
# 		opacity: 0.9;
# 		font-size: 22px;
#         margin: 0 5px;
#     }
# 	table.table td a {
# 		font-weight: bold;
# 		color: #566787;
# 		display: inline-block;
# 		text-decoration: none;
# 		outline: none !important;
# 	}
# 	table.table td a:hover {
# 		color: #2196F3;
# 	}
# 	table.table td a.edit {
#         color: #FFC107;
#     }
#     table.table td a.delete {
#         color: #F44336;
#     }
#     table.table td i {
#         font-size: 19px;
#     }
# 	table.table .avatar {
# 		border-radius: 50%;
# 		vertical-align: middle;
# 		margin-right: 10px;
# 	}
#     .pagination {
#         float: right;
#         margin: 0 0 5px;
#     }
#     .pagination li a {
#         border: none;
#         font-size: 13px;
#         min-width: 30px;
#         min-height: 30px;
#         color: #999;
#         margin: 0 2px;
#         line-height: 30px;
#         border-radius: 2px !important;
#         text-align: center;
#         padding: 0 6px;
#     }
#     .pagination li a:hover {
#         color: #666;
#     }	
#     .pagination li.active a, .pagination li.active a.page-link {
#         background: #03A9F4;
#     }
#     .pagination li.active a:hover {        
#         background: #0397d6;
#     }
# 	.pagination li.disabled i {
#         color: #ccc;
#     }
#     .pagination li i {
#         font-size: 16px;
#         padding-top: 6px
#     }
#     .hint-text {
#         float: left;
#         margin-top: 10px;
#         font-size: 13px;
#     }    
# 	/* Custom checkbox */
# 	.custom-checkbox {
# 		position: relative;
# 	}
# 	.custom-checkbox input[type="checkbox"] {    
# 		opacity: 0;
# 		position: absolute;
# 		margin: 5px 0 0 3px;
# 		z-index: 9;
# 	}
# 	.custom-checkbox label:before{
# 		width: 18px;
# 		height: 18px;
# 	}
# 	.custom-checkbox label:before {
# 		content: '';
# 		margin-right: 10px;
# 		display: inline-block;
# 		vertical-align: text-top;
# 		background: white;
# 		border: 1px solid #bbb;
# 		border-radius: 2px;
# 		box-sizing: border-box;
# 		z-index: 2;
# 	}
# 	.custom-checkbox input[type="checkbox"]:checked + label:after {
# 		content: '';
# 		position: absolute;
# 		left: 6px;
# 		top: 3px;
# 		width: 6px;
# 		height: 11px;
# 		border: solid #000;
# 		border-width: 0 3px 3px 0;
# 		transform: inherit;
# 		z-index: 3;
# 		transform: rotateZ(45deg);
# 	}
# 	.custom-checkbox input[type="checkbox"]:checked + label:before {
# 		border-color: #03A9F4;
# 		background: #03A9F4;
# 	}
# 	.custom-checkbox input[type="checkbox"]:checked + label:after {
# 		border-color: #fff;
# 	}
# 	.custom-checkbox input[type="checkbox"]:disabled + label:before {
# 		color: #b8b8b8;
# 		cursor: auto;
# 		box-shadow: none;
# 		background: #ddd;
# 	}
# 	/* Modal styles */
# 	.modal .modal-dialog {
# 		max-width: 400px;
# 	}
# 	.modal .modal-header, .modal .modal-body, .modal .modal-footer {
# 		padding: 20px 30px;
# 	}
# 	.modal .modal-content {
# 		border-radius: 3px;
# 	}
# 	.modal .modal-footer {
# 		background: #ecf0f1;
# 		border-radius: 0 0 3px 3px;
# 	}
#     .modal .modal-title {
#         display: inline-block;
#     }
# 	.modal .form-control {
# 		border-radius: 2px;
# 		box-shadow: none;
# 		border-color: #dddddd;
# 	}
# 	.modal textarea.form-control {
# 		resize: vertical;
# 	}
# 	.modal .btn {
# 		border-radius: 2px;
# 		min-width: 100px;
# 	}	
# 	.modal form label {
# 		font-weight: normal;
# 	}
# </style>
#   <body>
#     <div class="container">
#         <div class="table-wrapper">
#             <div class="table-title">
#                 <div class="row">
#                     <div class="col-sm-6">
# 						<h2>Manage <b>Notes</b></h2>
# 					</div>
# 					<div class="col-sm-6">
# 						<a href="#addEmployeeModal" class="btn btn-success" data-toggle="modal"><i class="material-icons">&#xE147;</i> <span>Add New Notes</span></a>
# 					</div>
#                 </div>
#             </div>
#             <table class="table table-striped table-hover">
#                 <thead>
#                     <tr>
# 						<th>
# 							<span class="custom-checkbox">
# 								<input type="checkbox" id="selectAll">
# 								<label for="selectAll"></label>
# 							</span>
# 						</th>
#                         <th>Name</th>
# 						<th>Description</th>
#                         <th>Actions</th>
#                     </tr>
#                 </thead>


#                 <tbody id="table-body">

#                 </tbody>


#             </table>
			
#         </div>
#     </div>

# 	<!-- Edit Modal HTML -->
# <!-- Add Note Modal -->
# <div id="addEmployeeModal" class="modal fade">
# 	<div class="modal-dialog">
# 		<div class="modal-content">
# 			<form id="add_or_edii_NoteForm">
# 				<div class="modal-header">
# 					<h4 class="modal-title">Add Note</h4>
# 					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
# 				</div>
# 				<div class="modal-body">
# 					<div class="form-group">
# 						<label>Title</label>
# 						<input type="text" class="form-control" id="noteTitle" required>
# 					</div>

# 					<div class="form-group">
# 						<label>Description</label>
# 						<textarea class="form-control" id="noteDescription" required></textarea>
# 					</div>
# 				</div>
# 				<div class="modal-footer">
# 					<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
# 					<input type="submit" class="btn btn-success" value="Add">
# 				</div>
# 			</form>
# 		</div>
# 	</div>
# </div>


# </div>

# 	    <!-- Edit Note Modal -->
# 		<div id="editEmployeeModal" class="modal fade">
# 			<div class="modal-dialog">
# 				<div class="modal-content">
# 					<form id="editNoteForm">
# 						<div class="modal-header">
# 							<h4 class="modal-title">Edit Note</h4>
# 							<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
# 						</div>
# 						<input type="hidden" id="editNoteId" value="">
# 						<div class="modal-body">
# 							<div class="form-group">
# 								<label>Title</label>
# 								<input type="text" id="editNoteTitle" class="form-control" required>
# 							</div>
	
# 							<div class="form-group">
# 								<label>Description</label>
# 								<textarea id="editNoteDescription" class="form-control" required></textarea>
# 							</div>
# 						</div>
# 						<div class="modal-footer">
# 							<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
# 							<input type="submit" class="btn btn-info" value="Save">
# 						</div>
# 					</form>
# 				</div>
# 			</div>
# 		</div>
# 	</div>


# 	<!-- Delete Modal HTML -->
# 	<div id="deleteEmployeeModal" class="modal fade">
# 		<div class="modal-dialog">
# 			<div class="modal-content">
# 				<form>
# 					<div class="modal-header">						
# 						<h4 class="modal-title">Delete Note</h4>
# 						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
# 					</div>
# 					<div class="modal-body">					
# 						<p>Are you sure you want to delete these Records?</p>
# 						<p class="text-warning"><small>This action cannot be undone.</small></p>
# 					</div>
# 					<div class="modal-footer">
# 						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
# 						<input type="submit" class="btn btn-danger" value="Delete">
# 					</div>
# 				</form>
# 			</div>
# 		</div>
# 	</div>


# </body>
# </html>

# <script>

# // function for create an note
   
#     function addNote() {
#         const noteTitle = document.getElementById('noteTitle').value;
#         const noteDescription = document.getElementById('noteDescription').value;

#         // Make API call to create or update note
#         fetch('http://127.0.0.1:8000/api/home/notes/create-or-update-notes', {
#             method: 'POST',
#             headers: {
#                 'Content-Type': 'application/json',
#             },
#             body: JSON.stringify({
#                 title: noteTitle,
#                 description: noteDescription,
#             }),
#         })
#         .then(response => response.json())
#         .then(data => {
#             if (data.status && data.status_code === 201) {
#                 // Note added successfully, you can update the UI if needed
#                 console.log('Note added successfully');
#                 location.reload(); // Refresh the screen
#             } else {
#                 console.error('Error adding note:', data.errors);
#             }
#         })
#         .catch(error => console.error('Error adding note:', error));
#     }

#     // Event listener for form submission
#     document.getElementById('add_or_edii_NoteForm').addEventListener('submit', function (event) {
#         event.preventDefault(); // Prevent the default form submission
#         addNote(); // Call the addNote function
#         $('#addEmployeeModal').modal('hide'); // Close the modal
#     });

#    // Function to delete a note by its ID
#    function deleteNote(id) {
# 	// Make API call to delete note
# 	fetch(`http://127.0.0.1:8000/api/home/notes/destroy-notes`, {
# 		method: 'DELETE',
# 		headers: {
# 			'Content-Type': 'application/json',
# 		},
# 		body: JSON.stringify({
# 			instance_id: [id],
# 		}),
# 	})
# 	.then(response => response.json())
# 	.then(data => {
# 		if (data.status && data.status_code === 200) {
# 			// Note deleted successfully, you can update the UI if needed
# 			console.log(`Note with ID ${id} deleted successfully`);
# 		} else {
# 			console.error('Error deleting note:', data.errors);
# 		}
# 	})
# 	.catch(error => console.error('Error deleting note:', error));
# }

# // Fetch data from the API
# fetch('http://127.0.0.1:8000/api/home/notes/get-notes-view')
# 	.then(response => response.json())
# 	.then(data => {
# 		if (data.status && data.status_code === 200) {
# 			const tableBody = document.getElementById('table-body');

# 			// Loop through the results and populate the table
# 			data.data.forEach(note => {
# 				const row = document.createElement('tr');
# 				row.innerHTML = `
# 					<td>
# 						<span class="custom-checkbox">
# 							<input type="checkbox" id="checkbox${note.id}" name="options[]" value="${note.id}">
# 							<label for="checkbox${note.id}"></label>
# 						</span>
# 					</td>
# 					<td>${note.title}</td>
# 					<td>${note.description}</td>
# 					<td>
# 						<a href="#editEmployeeModal" class="edit" data-toggle="modal" onclick="editNote(${note.id})"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
# 						<a href="#deleteEmployeeModal" class="delete" data-toggle="modal" onclick="deleteNote(${note.id})"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
# 					</td>
# 				`;
# 				tableBody.appendChild(row);
# 			});
# 		} else {
# 			console.error('Error fetching data:', data.errors);
# 		}
# 	})
# 	.catch(error => console.error('Error fetching data:', error));

# // Function to handle editNote click
# function editNote(instance_id) {
# 	fetch(`http://127.0.0.1:8000/api/home/notes/get-notes-view?id=${instance_id}`)
# 		.then(response => response.json())
# 		.then(data => {
# 			if (data.status && data.status_code === 200 && data.data.length > 0) {
# 				const note = data.data[0];

# 				// Update modal fields with the received data
# 				document.getElementById('editNoteId').value = note.id;
# 				document.getElementById('editNoteTitle').value = note.title;
# 				document.getElementById('editNoteDescription').value = note.description;

# 				// Show the modal
# 				$('#editEmployeeModal').modal('show');
# 			} else {
# 				console.error('Error retrieving note data:', data.errors);
# 			}
# 		})
# 		.catch(error => console.error('Error editing note:', error));
# }











# 	{% comment %} $(document).ready(function(){
# 		// Activate tooltip
# 		$('[data-toggle="tooltip"]').tooltip();
		
# 		// Select/Deselect checkboxes
# 		var checkbox = $('table tbody input[type="checkbox"]');
# 		$("#selectAll").click(function(){
# 			if(this.checked){
# 				checkbox.each(function(){
# 					this.checked = true;                        
# 				});
# 			} else{
# 				checkbox.each(function(){
# 					this.checked = false;                        
# 				});
# 			} 
# 		});
# 		checkbox.click(function(){
# 			if(!this.checked){
# 				$("#selectAll").prop("checked", false);
# 			}
# 		});
# 	}); {% endcomment %}
# </script>