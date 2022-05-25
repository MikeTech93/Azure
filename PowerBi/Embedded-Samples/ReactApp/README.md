## Instructions to run

1. Install NPM Packages
    npm install

2. Populate sampleReportUrl in demo/DemoApp.tsx with EmbedUrl, Token, TokenId, Expiration - These can be obtained from the NodeJS app in the embedData object that is returned

3. Run the react server
    npm run demo

4. Access the react app
    http://localhost:5300

5. You can now press the "Embed Report" button to load your report (The error handling is a little messed up so if it just continues to load then there is something wrong with the EmbedUrl object)