// Initialize Mermaid with custom configuration
document.addEventListener('DOMContentLoaded', function() {
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis'
            },
            sequence: {
                diagramMarginX: 50,
                diagramMarginY: 10,
                actorMargin: 50,
                width: 150,
                height: 65,
                boxMargin: 10,
                boxTextMargin: 5,
                noteMargin: 10,
                messageMargin: 35
            }
        });

        // Force render any mermaid diagrams
        setTimeout(function() {
            mermaid.init(undefined, document.querySelectorAll('.mermaid'));
        }, 1000);
    } else {
        console.error('Mermaid library not loaded');
    }
});

// Add PlantUML image error handling
document.addEventListener('DOMContentLoaded', function() {
    const plantumlImages = document.querySelectorAll('.plantuml img');

    plantumlImages.forEach(function(img) {
        img.onerror = function() {
            const container = img.parentElement;
            container.innerHTML = '<div class="diagram-error">Error loading PlantUML diagram. Please check your syntax or server connection.</div>';
        };
    });
});