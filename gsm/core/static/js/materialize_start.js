$(document).ready(function(){
        $('.modal').modal();
        $('select').formSelect();
        $('.dropdown-trigger').dropdown({ hover: true,
                      constrainWidth: false,
                      coverTrigger: false });
        $('.sidenav').sidenav({
        //edge: 'right',
            });
    });