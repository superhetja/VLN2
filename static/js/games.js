$(document).ready(function () {

    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/games?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="well game">
                                <a href="/games/${d.id}">
                                    <img class="game-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.price}$</p>
                                </a>
                            </div>`
                });
                $('.games').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                // TODO: show toastr
                console.error(error);
            }
        })
    });
});