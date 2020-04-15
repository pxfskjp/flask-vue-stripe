<template>
	<div>
		<h1>Home</h1>
		<p>The is the home page</p>
		<v-app>
      <v-content>
		 <v-carousel
    	cycle
    	height="400"
    	hide-delimiter-background
    	show-arrows-on-hover
  	>
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="display-3">{{ slide }}</div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>


  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="../assets/boardgames.jpg"
    >
      <v-card-title>Fucking Around</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Fun Family Hate</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Game Name</div>

      <div>Game Information</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Buy
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Rent
      </v-btn>
    </v-card-actions>
  </v-card>
	</v-content>
	</v-app>
	</div>
</template>


<script>
export default {
	name: 'Home',
	data() {
		return {
			colors: [
				'green',
				'red',
				'blue',
			],
			slides: [
				'Upcoming Tournaments',
				'Rent or Buy Games',
				'Information on Covid-19',
			],
		};
	},
};
</script>
