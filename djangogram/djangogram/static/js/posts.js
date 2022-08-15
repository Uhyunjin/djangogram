function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const handleLikeClick = (buttonId) => {
    console.log(buttonId);

    const likeButton = document.getElementById(buttonId);
    console.log(likeButton);

    const likeIcon = likeButton.querySelector("i");
    console.log(likeIcon);
    likeIcon.classList.replace("fa-heart-o", "fa-heart")

    const csrftoken = getCookie('csrftoken');
    console.log(csrftoken)

    //서버로 좋아요 api호출
    //결과를 받고 html(좋아요 하트) 모습을 변경
}