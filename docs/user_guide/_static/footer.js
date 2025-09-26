// footer.js - Documentation Library Footer Navigation
document.addEventListener('DOMContentLoaded', function() {
    // Find the main content area and add footer after it
    const contentWrap = document.querySelector('.wy-nav-content-wrap');
    const footer = document.querySelector('footer');
    
    if (footer) {
        // Create the library footer HTML
        const libraryFooter = document.createElement('div');
        libraryFooter.className = 'library-footer';
        libraryFooter.innerHTML = `
            <a href="/docs" class="library-footer-button">
                📚 Return to Documentation Library
            </a>
            <div class="library-footer-info">
                <strong>🎯 User Guide</strong> | Part of the Simple Cloud Kit Documentation Library
            </div>
        `;
        
        // Insert the footer after the existing footer
        footer.parentNode.insertBefore(libraryFooter, footer.nextSibling);
    }
});