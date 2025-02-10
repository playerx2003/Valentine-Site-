document.addEventListener("DOMContentLoaded", function () {
    const memes = document.querySelectorAll(".meme-gallery img");

    memes.forEach((meme) => {
        meme.addEventListener("click", function () {
            alert("😂 You found a funny one!");
        });
    });
});
