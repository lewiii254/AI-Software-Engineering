// write a function to
// find all images without alternate text
// and give them a red border
function findImagesWithoutAltText() {
            const images = document.querySelectorAll('img');

            images.forEach(image => {
                if (!image.alt) {
                    image.style.border = '2px solid red';
                }
            });
        }

        findImagesWithoutAltText();

        function calculateDaysBetweenDates(begin, end) {
            const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
            const firstDate = new Date(begin);
            const secondDate = new Date(end);
            const diffDays = Math.round(Math.abs((firstDate - secondDate) / oneDay));
            return diffDays;
        }