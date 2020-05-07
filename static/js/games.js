$(document).ready(function () {

    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/games?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="game col-xs-6 col-sm-4">
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

    function toggleSort(e) {
        e.preventDefault();
        for (let node of $('.sort-link')) {
            if (node.classList.toggle('sort-selected')) {
                let sortText = node.id;
                $.ajax({
                    url: '/games?sort_filter=' + sortText,
                    type: 'GET',
                    success: function(resp) {
                        let newHtml = resp.data.map(d => {
                            return `<div class="game col-xs-6 col-sm-4">
                                <a href="/games/${d.id}">
                                    <img class="game-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.price}$</p>
                                </a>
                            </div>`
                        });
                    $('.games').html(newHtml.join(''));
                    },
                    error: function (xhr, status, error) {
                    // TODO: show toastr
                    console.error(error);
                    },
                });
            }

        }
    };

    $('#price').on('click', function (e) {
        toggleSort(e);
    });

    $('#name').on('click', function (e) {
        toggleSort(e);
    });

    $('#types').on('change', function (e) {
        e.preventDefault();
        let val = this.value;
        $.ajax({
            url: val==0 ? '/games?sort_filter=name' : '/games?type_filter=' + val,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="game col-xs-6 col-sm-4">
                                <a href="/games/${d.id}">
                                    <img class="game-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.price}$</p>
                                </a>
                            </div>`
                });
                $('.games').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                // TODO: show toastr
                console.error(error);
            }
        })
    })
});
