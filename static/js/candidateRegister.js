const imagePreview = document.getElementById('UserPhoto')
const imageUploader = document.getElementById('UserUploader')

$(document).on("change", "#UserUploader", function(){
    console.log(this.files)
    var files = this.files
    var element
    var supportedImages = ["image/jpeg", "image/png"]
    
    element = files[0]
    imgcodified = URL.createObjectURL(element);
    document.getElementById('UserPhoto').setAttribute("src", imgcodified)


})

function createPreview(file){
    var img = $()

}
