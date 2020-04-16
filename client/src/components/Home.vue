<template>
	<div class="content">
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

<!-- ITEM CARDS -->
<v-container d-flex>
<v-card
    class="mx-auto"
    max-width="300"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src='https://cdn.shoplightspeed.com/shops/622104/files/18799131/768x768x2/wizards-of-the-coast-pre-order-magic-the-gathering.jpg'
			contain
    ></v-img>

    <v-card-subtitle class="pb-0">Magic: The Gathering</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>The collectable card game</div>
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
	<v-card
    class="mx-auto"
    max-width="300"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src='https://images-na.ssl-images-amazon.com/images/I/91Q9Uzy--fL._AC_SL1500_.jpg'
			contain
    ></v-img>

    <v-card-subtitle class="pb-0">Seasons</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>The tactical card game</div>
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
	<v-card
    class="mx-auto"
    max-width="300"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src='https://images-na.ssl-images-amazon.com/images/I/81crhhZd63L._AC_SL1500_.jpg'
			contain
    ></v-img>

    <v-card-subtitle class="pb-0">Gloomhaven</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>A table-top campaign for 1-4 players</div>
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
</v-container>
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
				'orange lighten-2',
				'deep-orange darken-1',
				'amber accent-3',
			],
			slides: [
				'Upcoming Tournaments',
				'Rent or Buy Games',
				'Information on Covid',
			],
		};
	},
};


</script>

<style scoped>
.content {
	margin-top: 4rem;
}
.v-card {
	height: 23rem;
	margin-top: 5rem;
	padding-top: 2rem;
};
.pb-0 {
	font-size: 2rem;
}
</style>
