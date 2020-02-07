function submitFavorite(event) {
    // let num = event.target.id.split("-")[1];
    // let text = $("#post-" + num).text();

    $.get("/add_favorite/", function (data) {
        if (data.data) {
            alert('Favorited successfully!')
        } else {
            alert('Could not be favorited...')
        }  
    });

}

$(window).on("load", function () {
    let buttons = $(".btn");

    buttons.each(function (index) {
        $(this).on("click", submitFavorite);
    });
});