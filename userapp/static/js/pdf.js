window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const invoice = this.document.getElementById("invoice");
            console.log(invoice);
            console.log(window);

            var opt = {
                margin: [0, 0, 0, 0], // Remove all margins: [top, right, bottom, left]
                filename: 'Certificate.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: {
                    scale: 0.75, // Set the scale to 75%
                    useCORS: true // Handle CORS for external images
                },
                jsPDF: {
                    unit: 'mm', // Use millimeters as unit
                    format: 'a4', // A4 paper size (210mm x 297mm)
                    orientation: 'portrait', // Portrait orientation
                    font: 'helvetica', // Font style
                    fontSize: 8, // Adjust font size if needed
                    hotfixes: ['px_scaling'], // Fix scaling issues in jsPDF
                    pageMargins: [0, 0, 0, 0] // Explicitly set the margins for jsPDF
                }
            };

            html2pdf().from(invoice).set(opt).save();
        });
}
