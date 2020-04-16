<template>
	<div>
		<h1 class="heading">Events</h1>
		<p class="subheading">We have events going on all the time! If you don't see one that suits you, contact us to book your own.</p>
	<v-row>
    <v-col
			class="wrapper">
      <v-sheet height="400" class="calendar">
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          :events="events"
          type="month"
        ></v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
	</div>
</template>


<script>

const today = new Date();
const dd = String(today.getDate()).padStart(2, '0');
const mm = String(today.getMonth() + 1).padStart(2, '0');
const yyyy = today.getFullYear();

const todayDate = `${yyyy}-${mm}-${dd}`;

export default {
	name: 'Events',
	data: () => ({
		today: todayDate,
		events: [
			{
				name: 'Adventurer\'s Guild',
				start: '2020-04-15',
			},
			{
				name: 'MTG Deck Building',
				start: '2020-04-19',
			},
			{
				name: 'Warhammer Tournamant',
				start: '2020-04-25',
			},
		],
	}),
	mounted() {
		this.$refs.calendar.scrollToTime('08:00');
	},
};

</script>

<style scoped>
.heading {
	margin-top: 7rem;
	font-size: 4rem;
	color: rgb(239,85,44);
}
.subheading {
	font-size: 1.3rem;
}
.wrapper {
	position: absolute;
	left: 0;
	right: 0;
}
.calendar {
	width: 100%;
}
</style>
