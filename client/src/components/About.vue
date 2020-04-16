<template>
  <v-card
    class="mx-auto"
    max-width="600"
  >
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-card-title v-text="card.title"></v-card-title>
          	<v-card-text v-html="card.text"></v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>


<script>
/* eslint-disable */
export default {
	name: 'About',
	data: () => ({
		cards: [
			{ title: 'About Us', text: 'With over 13,000 sq. ft. of display and gaming space, the Sentry Box is a Mecca for those interested in fantasy, science fiction, or military games, books and miniatures. The policy of the Sentry Box has always been If it is in print, we will try to stock it. With over 100,000 different items on the shelves, this shows that we mean what we say.', flex: 12 },
			{ title: 'Location', text: '1835 - 10th Ave SW <br/> Calgary, Alberta <br/> Canada T3C 0K2', flex: 6 },
			{ title: 'Hours', text: '11:00AM - 9:00PM Monday to Friday <br/> 10:00AM - 9:00PM Saturday <br/> 11:00AM - 6:00PM Sunday', flex: 6 },
			{ title: 'Phone', text: '403-245-2121 <br/> Toll-Free: 1-888-220-2121 <br/> Sentry Box Cards Phone: 403-457-9412' , flex: 6 },
			{ title: 'Parking', text: 'Available on both the east and west sides of the store. <br/> Accessible Parking and Entrance: Located on the east side with a ramp to our back door Please ring doorbell', flex: 6 },
		],
	}),
};
</script>

<style scoped>
.container {
	position: fixed;
	width: 50rem;
	height: 30rem;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
