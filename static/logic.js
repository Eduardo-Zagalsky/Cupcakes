let $flavor = $("#flavor").val();
let $size = $("#size").val();
let $rating = $("#rating").val();
let $img = $("#img").val();
let cupcakeData = { flavor: $flavor, size: $size, rating: $rating, img: $img };
$("submit").on("click", async function cupcakeForm() {
    await axios.post("/api/cupcakes", cupcakeData)
});

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