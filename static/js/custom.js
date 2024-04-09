let storeScroll = window.scrollY;
let htmlTag = document.getElementsByTagName('html');
document.addEventListener('scroll', () => {
  storeScroll = window.scrollY;
  if(storeScroll > 1) {
    htmlTag[0].setAttribute('data-scroll', 1);
  } else {
    htmlTag[0].setAttribute('data-scroll', 0);
  }
});

