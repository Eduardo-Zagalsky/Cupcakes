async function getCupcakes() {
    let $ul = $("#cupcake-list");
    let obj = await axios.get("/api/cupcakes");
    for (let i = 0; i < obj.data.cupcakes.length; i++) {
        let cupcake = obj.data.cupcakes[i].flavor;
        let $li = $("<li>");
        $li.append(cupcake);
        $ul.append($li);
    }
}

getCupcakes()