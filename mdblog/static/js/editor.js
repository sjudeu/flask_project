$(document).ready(function(){
    var simplemde = new SimpleMDE();

    $("form").on("submit", function(){
        html_render = simplemde.markdown(simplemde.value());
        $("#html_render").val(html_render)
    })
})
