$(document).ready(function () {
	$("#add_item").click(function () {
		var list = $("<li>").text("Item");
			$(".my_list").append(list);
		});
