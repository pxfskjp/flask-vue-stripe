<template>
	<div class="footer">
		<div class="smicons">
			<i class="fab fa-youtube"> YouTube</i>
			<i class="fab fa-twitter-square"> Twitter</i>
			<i class="fab fa-facebook-square"> Facebook</i>
			<i class="fab fa-wordpress"> Blog</i>
		</div>
    	<p>Copyright 2020 The Sentry Box - Site Development by The Bönor City Boys</p>
	</div>
</template>

<style scoped>
.footer {
	height: 5.5rem;
	position: absolute;
	bottom: 0;
	width: 100%;
  	background-color: black;
  	color: yellow;
  	text-align: center;
}
.smicons {
	font-size: 1.6rem;
	display: flex;
	justify-content: space-around;
	padding-top: 0.5rem;
	margin-bottom: .6em;
}

.fab:hover {
	cursor: pointer;
	color: rgb(146, 146, 13);
}


@media screen and (max-width: 800px) {
	.smicons {
		font-size: 1.2rem;
	}
	.fab:hover {
		cursor: text;
	}
	p {
		font-size: .8rem;
	}
}
</style>
