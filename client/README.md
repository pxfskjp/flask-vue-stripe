# client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Hosting

Navigate to client  
>npm run build  
>Firebase init  
>(*)hosting  
>use and existing project  
>use dist for your public directory  
>configure as SPA reqrite all urls to /index.html - yes  
> file dist/index.html already exists. overwrite? n  

inside the Books.vue (probably a better place to put this):  
under <script>  
>const GAMESAPI = 'https://games-api-juues42ia-uc.a.run.app';  
this URL is taken from the top of the games-api URL page thing  

replace the 'http://localhost:5000' with:  
${GAMESAPI}

Then... fuck, I dunno, I guess do the  
>npm run build  
>firebase deploy  
then also is that doesn't change anything...  
Go to cloud run, and then edit and revision, select the url to be the project and then select the latest update  
Then npm run build  
Then firebase deploy?
