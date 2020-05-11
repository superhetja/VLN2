$(document).ready(function () {

    function reloadGames (url, value) {
        $.ajax({
            url: url + (value ? value : ''),
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="game col-xs-6 col-sm-4">
                               <a href="/games/${d.id}">
                               <img class="game-img" src="${d.image}" alt="${d.name}"/>
                               <h4>${d.name}</h4>
                               <p>${d.price}$</p>
                               </a>
                           </div>`
                });
                $('.games').html(newHtml.join(''));
                },
            error: function (xhr, status, error) {
                console.error(error);
                },
        });
    }

    function populateStorage (text) {
        let storage = localStorage.getItem('searchHistory')
        if (storage !== null) {
            storage += '|' + text;
            localStorage.setItem('searchHistory', storage);
        } else {
            localStorage.setItem('searchHistory', text);
        }
    }

    function toggleSort(e) {
        e.preventDefault();
        for (let node of $('.sort-link')) {
            if (node.classList.toggle('sort-selected')) {
                let sortText = node.id;
                reloadGames('/games?sort_filter=', sortText)
            }
        }
    }


    $('#history-btn').on('click', function (e) {
        e.preventDefault();
        let history = localStorage.getItem('searchHistory').split('|');
        let newHtml = history.map( x => {
            return `<a class="dropdown-item" id="${x}" href="#">${x}</a>`
        });
        $('#history-dropdown').html(newHtml.join(''));
        $('.dropdown-item').on('click', function (e) {
            e.preventDefault();
            let searchText = this.id;
            reloadGames('/games?search_filter=', searchText);
        })
    })



    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let textField = $('#search-box')
        let searchText = textField.val();
        populateStorage(searchText);
        reloadGames('/games?search_filter=', searchText);
        textField.val('');
    });


    $('#price').on('click', function (e) {
        toggleSort(e);
    });

    $('#name').on('click', function (e) {
        toggleSort(e);
    });

    $('#types').on('change', function (e) {
        e.preventDefault();
        let val = this.value;
        val==='0' ? reloadGames('/games?sort_filter=name') : reloadGames('/games?type_filter=', val);
    })
});
