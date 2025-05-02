## write a function to find all images without alternate text and give them a red border
def findImagesWithoutAltText():
    images = document.querySelectorAll('img')

    images.forEach(image => {
        if (!image.alt) {
            image.style.border = '2px solid red'
        }
    })

    return images