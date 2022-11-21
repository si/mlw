module.exports = function (eleventyConfig) {

    eleventyConfig.addPassthroughCopy({ "src/images" : "images"});
    eleventyConfig.addPassthroughCopy({ "src/admin" : "admin"});
    eleventyConfig.addPassthroughCopy('src/_redirects');
      
    eleventyConfig.addCollection("seasonTagsList", function(collectionApi) {
        const tagsList = new Set();
        collectionApi.getAll().map( item => {
            if (item.data.tags) { // handle pages that don't have tags
                //item.data.tags.map( tag => tagsList.add(tag))
                item.data.tags.filter(a => a.startsWith('Season')).map( tag => tagsList.add(tag))
            }
        });
        return tagsList;
    });

    return {
        dir: {
            input: "src/views",
            output: "dist",
            includes: "_includes/partials",
            layouts: "_includes/layouts"
        },
        templateFormats: ["md", "njk"],
        markdownTemplateEngine: "njk",
        passthroughFileCopy: true
    };
};