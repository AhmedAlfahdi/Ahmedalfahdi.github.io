hljs.initHighlightingOnLoad()

var converter = new showdown.Converter({
    tables: true,
    strikethrough: true,
    tasklists: true,
    emoji: true,
    openLinksInNewWindow: true
})

var source = $('.md')
var html = converter.makeHtml(source.text())
source.html(html)