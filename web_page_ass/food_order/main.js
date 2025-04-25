const all_img=document.getElementsByTagName("img");
console.log(all_img)
for(let i=0;i<all_img.length;i++){
    all_img[i].src=`./static/img${(i+1)%8}.jpg`;
}
